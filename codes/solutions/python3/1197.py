from functools import lru_cache

from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i == j == 0:
                return 0
            if i == 1 and j == 0 or j == 1 and i == 0:
                return float('inf')
            return min(dfs(abs(i - 2), abs(j - 1)), dfs(abs(i - 1), abs(j - 2))) + 1

        return dfs(abs(x), abs(y))

    def minKnightMoves2(self, x: int, y: int) -> int:
        queue = deque()
        queue.append([0, 0])
        moves = 0
        visited = set()
        while queue:
            s = len(queue)
            while s:
                i, j = queue.popleft()
                if i == x and j == y: return moves
                for u, v in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)):
                    if (i + u, j + v) not in visited and i + u >= -2 and j + v >= -2:
                        queue.append((u, v))
                        visited.add((i + u, j + v))
                s -= 1



print(Solution().minKnightMoves2(2, 1))
