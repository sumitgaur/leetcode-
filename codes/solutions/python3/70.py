class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i >= n: return 1 if i == n else 0
            if i not in memo:
                memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        return dfs(0)

    def climbStairs2(self, n: int) -> int:
        l=[1,2]
        for i in range(2, n):
            l.append(l[i-1]+l[i-2])
        return l[n-1]

print(Solution().climbStairs2(5))
