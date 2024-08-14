import collections


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.arr = collections.deque(maxlen=size)

    def next(self, val: int) -> float:
        self.arr.append(val)
        return sum(self.arr) / len(self.arr)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

class MovingAvg:
    def __init__(self, size):
        self.dq = collections.deque()
        self.size = size
        self.sum = 0

    def next(self, x):
        if len(self.dq) == self.size:
            self.sum -= self.dq.popleft()
        self.dq.append(x)
        self.sum += x
        print(self.sum // len(self.dq))


class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.s = 0
        self.cnt = 0

    def next(self, x):
        idx = self.cnt % self.size
        self.s += x - self.arr[idx]
        self.idx = x
        self.cnt += 1
        return self.s / min(self.cnt, self.size)
    m


mv = MovingAvg(3)
mv.next(1)
mv.next(10)
mv.next(3)
mv.next(5)
