import bisect


class RecentCounter:

    def __init__(self):
        self.p = []

    def ping(self, t):
        self.p.append(t)
        i = bisect.bisect_left(self.p, t - 3000)
        self.p = self.p[i:]
        return len(self.p)


rc = RecentCounter()
print(rc.ping(1))
print(rc.ping(100))
print(rc.ping(3001))
print(rc.ping(3002))
