import collections
import time


class SlidingWindow:
    TIME = 60  # 10sec
    _CAPACITY = 10
    queue = collections.deque()

    def __init__(self):
        pass

    def checkRequest(self):
        while self.queue and self.queue[0]['in_time'] > time.time() - self.TIME:
            self.queue.popleft()
        if len(self.queue) > self._CAPACITY:
            return False
        else:
            self.queue.append({'in_time': time.time()})
