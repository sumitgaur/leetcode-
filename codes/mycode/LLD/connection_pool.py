import sqlite3
import threading
import time
from abc import ABC, abstractmethod


class ConnectionPoolException(Exception):
    pass


class NoAvailableConnectionException(ConnectionPoolException):
    pass


class SQLConnectionException(ConnectionPoolException):
    pass


class PooledConnection:
    def __init__(self, db: str, ttl: int):
        self.db = db
        self.ttl = ttl
        self.conn = sqlite3.connect(db, timeout=ttl)
        self.expiry = time.time() + ttl
        self.in_use = False

    def is_expired(self):
        return time.time() > self.expiry

    def refresh(self):
        self.close()
        self.conn = sqlite3.connect(self.db, timeout=self.ttl)
        self.expiry = time.time() + self.ttl

    def close(self):
        try:
            self.conn.close()
        except Exception:
            pass


class ConnectionPool(ABC):
    @abstractmethod
    def getConnection(self) -> [NoAvailableConnectionException, SQLConnectionException]:
        pass

    @abstractmethod
    def releaseConnection(self, conn) -> None:
        pass

    @abstractmethod
    def closeAll(self):
        pass


class ConnectionPoolImpl(ConnectionPool):
    instance = None

    def __init__(self, db='example.db', max_pool_size=10, ttl=60):
        self.db = db
        self.max_pool_size = max_pool_size
        self.ttl = ttl
        self.pool = []
        self.lock = threading.Lock()

    @classmethod
    def getInstance(cls, k):
        if not cls.instance:
            cls.instance = ConnectionPoolImpl(k)
        return cls.instance

    def getConnection(self):
        with self.lock:
            # Reuse available connection
            for pc in self.pool:
                if not pc.in_use:
                    if pc.is_expired():
                        pc.refresh()
                    pc.in_use = True
                    return pc

            # Create new connection if possible
            if len(self.pool) < self.max_pool_size:
                pc = PooledConnection(self.db, self.ttl)
                pc.in_use = True
                self.pool.append(pc)
                return pc

            raise NoAvailableConnectionException("No available connection in pool")

    def releaseConnection(self, conn) -> None:
        conn.is_available = True

    def closeAll(self):
        for pc in self.pool:
            pc.close()
        self.pool.clear()


pool = ConnectionPoolImpl(max_pool_size=2)

conn1 = pool.getConnection()
conn2 = pool.getConnection()

pool.releaseConnection(conn1)
conn3 = pool.getConnection()  # reused

pool.closeAll()
