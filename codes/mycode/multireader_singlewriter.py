import time
from threading import Thread, Lock, Semaphore


class SharedResource:
    MAX_READERS = 10  # put some higher value because semaphore require some max capacity

    def __init__(self):
        self.rsemaphore = Semaphore(SharedResource.MAX_READERS)
        self.wlock = Lock()


class Reader:
    def __init__(self, name, resource):
        self.name = name
        self.resource = resource

    def read(self):
        while self.resource.wlock.locked():
            continue
        self.resource.rsemaphore.acquire()
        print(f'Reader {self.name} reading data')
        time.sleep(1)
        print(f'Reader {self.name} reading done')
        self.resource.rsemaphore.release()

class Writer:
    def __init__(self, name, resource):
        self.name = name
        self.resource = resource

    def write(self):
        while self.resource.rsemaphore._value != SharedResource.MAX_READERS:  # all semaphores are released means no one is reading
            continue
        self.resource.wlock.acquire()
        print(f'Writer {self.name} writing data')
        time.sleep(2)
        print(f'Writer {self.name} writing done')
        self.resource.wlock.release()


if __name__ == '__main__':
    sr = SharedResource()
    reader1 = Reader("reader1", sr)
    reader2 = Reader("reader2", sr)
    reader3 = Reader("reader3", sr)
    writer1 = Writer("writer1", sr)
    writer2 = Writer("writer2", sr)

    Thread(target=reader1.read).start()
    Thread(target=writer1.write).start()
    time.sleep(2)
    Thread(target=reader2.read).start()
    Thread(target=writer2.write).start()
    Thread(target=reader3.read).start()
