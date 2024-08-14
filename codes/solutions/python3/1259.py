from functools import cache


class Solution:
    def numberOfWays(self, num_people):
        self.memo = {0: 1}

        def dp(n):
            if n not in self.memo:
                self.memo[n] = sum(
                    [dp(i - 2) * dp(n - i) for i in range(2, n + 1, 2)]
                ) % (10 ** 9 + 7)
            return self.memo[n]

        return dp(num_people)

    def numberOfWays(self, numPeople: int) -> int:
        @cache
        def dfs(i: int) -> int:
            if i < 2:
                return 1
            ans = 0
            for l in range(0, i, 2):
                r = i - l - 2
                ans += dfs(l) * dfs(r)
                ans %= mod
            return ans

        mod = 10 ** 9 + 7
        return dfs(numPeople)
