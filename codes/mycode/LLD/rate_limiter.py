from collections import deque, defaultdict


class RateLimiter:
    # sliding windows   Allow N requests in T window
    def __init__(self, max_requests, T):
        self.max_requests = max_requests
        self.window_size = T
        self.user_requests = defaultdict(deque)

    def allow(self, user_id, t):
        queue = self.user_requests[user_id]
        while queue and queue[0] <= t - self.window_size:
            queue.popleft()
        if len(queue) < self.window_size:
            queue.append(t)
            return True
        else:
            return False


