"""
Problem statement
1. Multiple log levels (DEBUG,INFO,WARNING)
2. Multiple Output (Console,File,Remote/HTTP,DB)
3. Ability to log to multiple destinations simultaneously
4. Runtime Configurability
5. Extensibility(add new loggers without changing the existing code)
"""
import threading
import time
from abc import ABC, abstractmethod
import sqlite3
from enum import IntEnum


class LogLevel(IntEnum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40


class LogRecord:

    def __init__(self, level, message):
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.message = message
        self.level = level


class Formatter(ABC):

    def format(self, record: LogRecord):
        return f"{record.timestamp} [{record.level.name}] {record.message}"


class LogHandler(ABC):
    def __init__(self, level: LogLevel, formatter):
        self.level = level
        self.formatter = formatter

    def handle(self, record: LogRecord):
        if record.level >= self.level:
            self.emit(record)

    @abstractmethod
    def emit(self, record: LogRecord):
        pass


"""Concrete handlers"""


class ConsoleHandler(LogHandler):

    def emit(self, record: LogRecord):
        print(self.formatter.format(record))


class FileHandler(LogHandler):
    def __init__(self, level, file_path, formatter):
        super().__init__(level, formatter)
        self.file_path = file_path

    def emit(self, record: LogRecord):
        with open(self.file_path, 'a') as f:
            f.write(self.formatter.format(record))


class DbHandler(LogHandler):
    def __init__(self, level, db_path, formatter):
        super().__init__(level, formatter)
        self.lock = threading.Lock()
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)  # could use connection pool for reusing the connections
        self._init_db()

    def _init_db(self):
        self.connection.execute("""
                CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    level TEXT,
                    message TEXT
                )
            """)
        self.connection.commit()

    def emit(self, record: LogRecord):
        with self.lock:
            sql = f'INSERT INTO logs (timestamp,level,message) VALUES {record.timestamp},{record.level},{record.message}'
            self.connection.execute(sql)
            self.connection.commit()


class RemoteHandler(LogHandler):

    def emit(self, record: LogRecord):
        print(f"Sending to remote {self.formatter.format(record)}")


# Facade layer
class Logger:
    def __init__(self):
        self.handlers = []

    def add_handler(self, hander):
        self.handlers.append(hander)

    def log(self, level, message):
        record = LogRecord(level, message)
        for handler in self.handlers:
            handler.handle(record)

    def info(self, message):
        self.log(LogLevel.INFO, message)

    def debug(self, message):
        self.log(LogLevel.DEBUG, message)

    def warning(self, message):
        self.log(LogLevel.WARNING, message)

    def error(self, message):
        self.log(LogLevel.ERROR, message)


formatter = Formatter()
logger = Logger()
logger.add_handler(ConsoleHandler(LogLevel.INFO, formatter))
logger.add_handler(FileHandler(LogLevel.DEBUG, "app.log", formatter))
logger.add_handler(RemoteHandler(LogLevel.ERROR, formatter))
logger.info("Info started ")
logger.error("Error coming")
logger.debug("Debugging started")
