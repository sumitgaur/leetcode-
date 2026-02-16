"""
Real life: Detect suspicious activity

Problem

<timestamp> <user_id> <amount>


Tasks

Detect users with > N transactions in last X minutes

Detect sudden spikes in amount

Tests

Sliding window

Deques

Time-based pruning
"""
import datetime
import time
from collections import deque, defaultdict


class Transaction:
    def __init__(self, trans_str):
        ts, user, amt = trans_str.split()
        self.timestamp = datetime.datetime.fromisoformat(ts).timestamp()
        self.user_id = user
        self.amount = amt


def detect_fraud(transactions_str, n, x):
    transactions = [Transaction(t) for t in transactions_str]
    freq_mp = defaultdict(int)
    now = time.time()
    dq = deque()
    frauds = set()
    for trans in transactions:
        dq.append(trans)
        freq_mp[trans.user_id] += 1
        if freq_mp[trans.user_id] > n: frauds.add(trans.user_id)
        while dq and dq[0].timestamp < now - x:
            t = dq.popleft()
            freq_mp[t] -= 1
    return frauds


def detect_spike(transactions_str,):
    transactions = [Transaction(t) for t in transactions_str]

logs = [
    "2025-01-14T10:00:00 userA 100",
    "2025-01-14T10:01:00 userB 50",
    "2025-01-14T10:02:00 userA 200",
    "2025-01-14T10:03:00 userA 300",
    "2025-01-14T10:04:00 userB 60",
]
N = 2
WINDOW_MIN = 5


print(detect_fraud(logs, N, WINDOW_MIN))
