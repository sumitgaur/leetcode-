import bisect
import random


class Solution:

    def __init__(self, N, blacklist):
        self.forbidden, self.n, self.used, self.cur = set(blacklist), N, set(), 0

    def pick(self):
        while self.cur in self.forbidden: self.cur += 1
        if self.cur < self.n:
            num, self.cur = self.cur, self.cur + 1
        else:
            num = self.used.pop()
        self.used.add(num)
        return num

""
class Solution_2:
    def __init__(self, N, blacklist):
        self.N = N
        self.blacklist = sorted(blacklist)
        i, self.allowed_ranges = 0, []
        for x in self.blacklist:
            self.allowed_ranges.append([(i, x - 1), x - i]) if x - 1 >= i else None
            i = x + 1
        self.allowed_ranges.append([(i, N - 1), N - i]) if N - 1 >= i else None

        self.counts = [0] * len(self.allowed_ranges)
        for i in range(len(self.allowed_ranges)):
            self.counts[i] = self.counts[i - 1] + self.allowed_ranges[i][1]

    def pick(self):
        x = random.randint(0, self.N - len(self.blacklist) - 1)
        selected_range = self.allowed_ranges[bisect.bisect_right(self.counts, x)]
        return random.randint(selected_range[0][0], selected_range[0][1])


sol = Solution(7, [2, 3, 5])
for _ in range(10):
    print(sol.pick())
