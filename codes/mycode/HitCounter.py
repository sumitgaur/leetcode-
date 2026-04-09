import time
from collections import OrderedDict


class HitCounter:
    def __init__(self, window):
        self.mp = OrderedDict()
        self.window = window

    def add_event(self, ts, device_id):  # O(1)
        if device_id:
            self.mp.pop(device_id)
        self.mp[device_id] = ts
        self._evict(ts)

    def _evict(self, current_ts):  # Amortized O(1)
        while self.mp:
            device_id, ts = next(iter(self.mp.items()))
            if ts < current_ts - self.window:
                self.mp.popitem(last=False)
            else:
                break

    def get_count(self):  # O(1)
        self._evict(time.time())
        return len(self.mp)



from collections import defaultdict


class HitCounter:
    def __init__(self, window=300):
        self.window = window
        self.buckets = defaultdict(set)  # second -> set(device_ids)

    def add_event(self, ts, device_id):
        self.buckets[ts].add(device_id)

    def get_count(self, query_ts):
        start = query_ts - self.window
        devices = set()

        for t in range(start, query_ts + 1):
            if t in self.buckets:
                devices |= self.buckets[t]

        return len(devices)
