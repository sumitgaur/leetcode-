import heapq
from queue import PriorityQueue


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x ** 2 + self.y ** 2 > other.x ** 2 + other.y ** 2


class Solution:
    def kClosest(self, points, K):
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:K]

    def kclosest2(self, points, K):
        hp = [(-(x * x + y * y), (x, y)) for x, y in points[:K]]
        heapq.heapify(hp)
        for x, y in points[K:]:
            heapq.heappushpop(hp, (-(x * x + y * y), (x, y)))
        return [(x, y) for _, (x, y) in hp]

    def kclosest3(self, points, K):
        hp = [Point(x, y) for x, y in points[:K]]
        heapq.heapify(hp)
        for x, y in points[K:]:
            heapq.heappushpop(hp, Point(x, y))
        return [[p.x, p.y] for p in hp]


points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(Solution().kclosest3(points, k))
