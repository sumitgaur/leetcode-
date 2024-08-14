from typing import List


class Solution:
    def maxSubArray(self, nums):
        sm, mn, mx = 0, 0, -float("inf")
        for num in nums:
            sm += num
            mx, mn = max(mx, sm - mn), min(mn, sm)
        return mx

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mx = mn = mx_till_here = mn_till_here = nums[0]
        a = []
        b = []
        for x in nums:
            mx_till_here = max(x, mx_till_here + x)
            mn_till_here = min(x, mn_till_here + x)
            mx = max(mx_till_here, mx)
            mn = min(mn_till_here, mn)
            a.append(mx_till_here)
            b.append(mn_till_here)
        print(a)
        print(b)
        return max(abs(mx), abs(mn))


nums = [-7, -1, 0, -2, 1, 3, 8, -2, -6, -1, -10, -6, -6, 8, -4, -9, -4, 1, 4, -9]
Solution().maxAbsoluteSum(nums)
