from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs, t, m, n = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 2], 0, len(
            grid), len(grid[0])
        while bfs:
            new = []
            for i, j in bfs:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        new.append((x, y))
            bfs = new
            t += bool(bfs)
        return t if all(val != 1 for row in grid for val in row) else -1

    def orangesRotting2(self, grid: List[List[int]]) -> int:
        q = deque([(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2])
        min_time = 0
        while q and any(v for r in grid for v in r if v == 1):
            rotten = len(q)
            while rotten:
                rotten -= 1
                x, y = q.popleft()
                for (i, j) in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]) and grid[x + i][y + j] == 1:
                        q.append((x + i, y + j))
                        grid[x + i][y + j] = 2
            min_time += 1
        return -1 if any(v for r in grid for v in r if v == 1) else min_time


grid = [[1], [2], [1], [2]]
print(Solution().orangesRotting2(grid))
