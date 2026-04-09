from abc import ABC, abstractmethod
import time
import threading
from collections import defaultdict


class RateLimitStrategy(ABC):

    @abstractmethod
    def allow_request(self, key: str) -> bool:
        pass


class FixedWindowRateLimiter(RateLimitStrategy):

    def __init__(self, max_requests: int, window_size_seconds: int):
        self.max_requests = max_requests
        self.window_size = window_size_seconds

        self.windows = defaultdict(lambda: {"expiry": 0, "count": 0})
        self.lock = threading.Lock()

    def allow_request(self, key: str) -> bool:
        now = int(time.time())

        with self.lock:
            window = self.windows[key]

            if window["expiry"] < now:
                window["expiry"] = now + self.window_size
                window["count"] = 0

            if window["count"] < self.max_requests:
                window["count"] += 1
                return True

            return False


class TokenBucketRateLimiter(RateLimitStrategy):

    def __init__(self, capacity: int, refill_rate_per_sec: float):
        self.capacity = capacity
        self.refill_rate = refill_rate_per_sec

        self.buckets = {}
        self.lock = threading.Lock()

    def allow_request(self, key: str) -> bool:
        now = time.time()

        with self.lock:
            bucket = self.buckets.get(key)

            if bucket is None:
                bucket = {
                    "tokens": self.capacity,
                    "last_refill": now
                }
                self.buckets[key] = bucket

            # Refill tokens
            elapsed = now - bucket["last_refill"]
            refill = elapsed * self.refill_rate
            bucket["tokens"] = min(self.capacity, bucket["tokens"] + refill)
            bucket["last_refill"] = now

            if bucket["tokens"] >= 1:
                bucket["tokens"] -= 1
                return True

            return False


class RateLimiter:

    def __init__(self, strategy: RateLimitStrategy):
        self._strategy = strategy

    def allow(self, key: str) -> bool:
        return self._strategy.allow_request(key)

    def change_strategy(self, new_strategy: RateLimitStrategy):
        self._strategy = new_strategy



if __name__ == "__main__":
    limiter = RateLimiter(
        FixedWindowRateLimiter(max_requests=5, window_size_seconds=10)
    )

    user = "user-123"

    for i in range(7):
        print(f"Request {i + 1}: {limiter.allow(user)}")

    # Switch strategy dynamically
    limiter.change_strategy(
        TokenBucketRateLimiter(capacity=10, refill_rate_per_sec=1)
    )
