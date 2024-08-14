class Solution:
    def knightProbability(self, N, K, r, c):
        memo = {}

        def dfs(i, j, p, k):
            if 0 <= i < N and 0 <= j < N and k < K:
                sm = 0
                for x, y in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)):
                    if (i + x, j + y, k) not in memo:
                        memo[(i + x, j + y, k)] = dfs(i + x, j + y, p / 8, k + 1)
                    sm += memo[(i + x, j + y, k)]
                return sm
            else:
                return 0 <= i < N and 0 <= j < N and p or 0

        return dfs(r, c, 1, 0)

    def knightProbability2(self, n: int, k: int, row: int, column: int) -> float:
        memo = {}

        def dfs(n, k, i, j):
            if not (0 <= i < n and 0 <= j < n):
                return 0
            if k == 0:
                return 1
            if (k, i, j) not in memo:
                memo[(k, i, j)] = sum(1.0 / 8 * dfs(n, k - 1, i + x, j + y) for x, y in
                                      ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)))
            return memo[(k, i, j)]

        return dfs(n, k, row, column)


print(Solution().knightProbability2(3, 2, 0, 0))
