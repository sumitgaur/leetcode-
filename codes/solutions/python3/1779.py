import sys
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def _min(p1, p2):
            if p1[0] == p2[0] or p1[1] == p2[1]:
                return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
            return sys.maxsize

        min_index, p = min(enumerate(points), key=lambda p: _min(p[1], [x, y]))
        return min_index if p[0] == x or p[1] == y else -1

x = 3
y = 4
points = [[2,3]]
print(Solution().nearestValidPoint(x, y, points))
