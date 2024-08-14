import collections
import threading


# class BoundedBlockingQueue(object):
#     def __init__(self, capacity: int):
#         self.pushing = threading.Semaphore(capacity)
#         self.pulling = threading.Semaphore(0)
#         self.queue = collections.deque()
#
#     def enqueue(self, element: int) -> None:
#         self.pushing.acquire()
#         self.queue.append(element)
#         self.pulling.release()
#
#     def dequeue(self) -> int:
#         self.pulling.acquire()
#         self.pushing.release()
#         return self.queue.popleft()
#
#     def size(self) -> int:
#         return len(self.queue)
class BoundedBlockingQueue:
    def __init__(self, capacity):
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.capacity = capacity
        self.queue = collections.deque(maxlen=capacity)

    def enqueue(self, x):
        self.pushing.acquire()
        self.queue.appendleft(x)
        self.pulling.release()

    def dequeue(self):
        self.pulling.acquire()
        pop = self.queue.pop()
        self.pushing.release()
        return pop

    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    bbq = BoundedBlockingQueue(5)


    def producer():
        while True:
            bbq.enqueue(1)


    def consumer():
        while True:
            print(bbq.dequeue())


    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
