import collections


class HitCounter(object):

    def __init__(self):
        self.hits = []

    def hit(self, timestamp):
        heapq.heappush(self.hits, timestamp + 300)

    def getHits(self, timestamp):
        while self.hits and self.hits[0] <= timestamp:
            heapq.heappop(self.hits)
        return len(self.hits)


class HitCounter1:
    def __init__(self):
        self.dq = collections.deque()

    def hit(self, ts):
        self.dq.append(ts + 300)
        while self.dq and self.dq[0] <= ts:
            self.dq.popleft()

    def getHits(self, ts):
        while self.dq and self.dq[0] <= ts:
            self.dq.popleft()
        print(len(self.dq))


hc = HitCounter1()
hc.hit(1)
hc.hit(2)
hc.hit(3)
hc.getHits(4)
hc.hit(300)
hc.getHits(300)
hc.getHits(301)
