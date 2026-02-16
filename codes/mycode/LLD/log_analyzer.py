"""
You are given a list of log entries in the format
"<timestamp> <ip_address> <endpoint>"
"2025-12-15T10:01:22" 192.121.0.1 /users/user-id

find
1. Find top k ip addresses by the number of requests
2. Filter logs by time range
3. Find the most accessed endpoint
follow up
<do this for the large files>
"""
import datetime
from collections import Counter

from sortedcontainers import SortedList


class LogEntry:
    def __init__(self, log_str: str = None, timestamp=None, ip=None, endpoint=None):
        if log_str:
            timestamp, ip_address, endpoint = log_str.split()
            self.ip_address = ip_address
            self.endpoint = endpoint
        self.timestamp = datetime.datetime.fromisoformat(timestamp)

    def __repr__(self):
        return f"{self.timestamp.isoformat()} {self.ip_address} {self.endpoint}"

    def __lt__(self, other):
        return self.timestamp < other.timestamp


class LogAnalyzer:
    def __init__(self, log_entries):
        self.log_entries = [LogEntry(log) for log in log_entries]
        self.ips = list(map(lambda e: e.ip_address, self.log_entries))
        self.endpoints_ = list(map(lambda e: e.endpoint, self.log_entries))
        self.ip_freq_mp = Counter(self.ips)
        self.endpoints_mp = Counter(self.endpoints_)
        self.sorted_log_entries = SortedList(self.log_entries)

    def top_k_ip_address(self, k):
        return list(map(lambda x: x[0], self.ip_freq_mp.most_common(k)))

    def most_accessed_endpoint(self):
        return self.endpoints_mp.most_common()[0][0]

    def filter_by_range(self, start_time, end_time):
        l = self.sorted_log_entries.bisect_left(LogEntry(timestamp=start_time))
        r = self.sorted_log_entries.bisect_right(LogEntry(timestamp=end_time))
        return self.log_entries[l:r]


logs = [
    "2025-01-14T10:01:00 10.0.0.1 /login",
    "2025-01-14T10:02:00 10.0.0.2 /home",
    "2025-01-14T10:03:00 10.0.0.1 /home",
    "2025-01-16T10:04:00 10.0.0.3 /login",
    "2025-01-16T10:04:00 10.0.0.3 /login",
    "2025-01-16T10:05:00 10.0.0.1 /profile",
]

log_analyzer = LogAnalyzer(logs)
print(log_analyzer.top_k_ip_address(2))
print(log_analyzer.most_accessed_endpoint())
print(log_analyzer.filter_by_range("2025-01-14", "2025-01-15"))
