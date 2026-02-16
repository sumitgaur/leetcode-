from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zeros, res = [-1] + [i for i, c in enumerate(A) if not c] + [len(A)], 0
        for j in range(K + 1, len(zeros)):
            res = max(res, zeros[j] - zeros[j - K - 1] - 1)
        return res or K and len(A)


from collections import deque


class Solution2:
    def longestOnes(self, nums: List[int], k: int) -> int:
        s = 0
        res = -1
        zeroes_in_window = deque()
        for j in range(len(nums)):
            if nums[j] == 0:
                zeroes_in_window.append(j)
                if len(zeroes_in_window) > k:
                    s = zeroes_in_window.popleft() + 1
            res = max(j - s + 1, res)
        return res


nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3

print(Solution2().longestOnes(nums, k))
