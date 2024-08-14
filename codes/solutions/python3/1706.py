from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid and grid[0])
        answer = list(range(n))
        for i in range(m):
            for j in range(n):
                if answer[j] == -1:
                    continue
                cu_pos = answer[j]
                if grid[i][cu_pos] == 1:
                    if cu_pos + 1 == n or grid[i][cu_pos + 1] == -1:
                        answer[j] = -1
                    else:
                        answer[j] = answer[j] + 1
                else:
                    if cu_pos - 1 == -1 or grid[i][cu_pos - 1] == 1:
                        answer[j] = -1
                    else:
                        answer[j] = answer[j] - 1
        print(answer)


grid = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]

Solution().findBall(grid)
