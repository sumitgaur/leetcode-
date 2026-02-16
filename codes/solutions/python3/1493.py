from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = 0
        zeros = [i for i, c in enumerate(nums) if c == 0]
        if not zeros:
            return len(nums) - 1
        for j in range(len(zeros)):
            s = zeros[j - 1] + 1 if j - 1 >= 0 else 0
            e = zeros[j + 1] - 1 if j + 1 < len(zeros) else len(nums) - 1
            mx = max(mx, e - s)
        return mx


nums = [ 0, 1, 1, 1, 0, 0]
print(Solution().longestSubarray(nums))
