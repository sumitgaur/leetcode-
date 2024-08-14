from typing import List


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid and grid[0])
        visited = set()

        def dfs(grid, i, j):
            if i == m - 1 and j == n - 1:
                return True, 1
            if not (i < m and j < n) or grid[i][j] == 0 or (i, j) in visited:
                return False, 0
            visited.add((i, j))
            d, d_op = dfs(grid, i + 1, j)
            r, r_op = dfs(grid, i, j + 1)
            return d or r, d_op + r_op

        res, op = dfs(grid, 0, 0)
        return op < 2


grid = [[1, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 1, 1, 1]]
Solution().isPossibleToCutPath(grid)
