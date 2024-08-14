# class TimeMap:
#
    def __init__(self):
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ''


from collections import defaultdict
import bisect


class TimeMap:

    def __init__(self):
        self.values = defaultdict(list)
        self.ts = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append(value)
        self.ts[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect_left(self.ts[key], timestamp)
        return self.values[key][i]


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set(key, value, timestamp)
param_2 = obj.get(key, timestamp)
