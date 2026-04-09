from typing import List


class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        stack, nums, res = [(0, [], 0, k)], range(1, 10), []
        while stack:
            sm, tmp, index, k_val = stack.pop(0)
            for i in range(index, len(nums)):
                if sm + nums[i] < n and k_val > 0: stack.append((sm + nums[i], tmp + [nums[i]], i + 1, k_val - 1))
                elif sm + nums[i] == n and k_val == 1: res.append(tmp + [nums[i]])
        return res


class Solution1:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def do(k, n, cur, s):
            if k == 0 and n == 0:
                res.append(cur[:])
            for i in range(s, 10):
                if k > 0 and i <= n:
                    cur.append(i)
                    do(k - 1, n - i, cur, i + 1)
                    cur.pop()
                else:
                    break

        do(k, n, [], 1)
        return res


print(Solution1().combinationSum3(3,7))