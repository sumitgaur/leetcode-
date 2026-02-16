from typing import List


class Solution:

    def __init__(self, n_rows, n_cols):
        self.rows, self.cols, self.used = n_rows, n_cols, set()

    def flip(self):
        while True:
            r, c = random.randint(1, self.rows), random.randint(1, self.cols)
            if (r, c) not in self.used:
                self.used.add((r, c))
                return [r - 1, c - 1]

    def reset(self):
        self.used = set()


import random


class Solution2:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.swap_mp = {}

    def flip(self) -> List[int]:
        rand_i = random.randint(0, self.total - 1)
        choosen = self.swap_mp.get(rand_i, rand_i)
        self.total -= 1
        self.swap_mp[rand_i] = self.total
        return [choosen // self.n, choosen % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.swap_mp.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()

obj = Solution2(3, 1)
print(obj.flip())
print(obj.flip())
print(obj.flip())
obj.reset()
print(obj.flip())
