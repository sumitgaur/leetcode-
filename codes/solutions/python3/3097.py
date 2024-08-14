from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        or_ = 0
        best = len(nums)
        s, e = 0, 0
        while e < len(nums):
            or_ = nums[e] | or_
            if or_ >= k:
                best = min(best, e - s + 1)
                or_ = or_ | ~nums[s]
                s += 1
                if or_ >= k:
                    best = min(best, e - s + 1)

            e += 1
        print(best)
        return best


nums = [1,2,32,21]
k = 55
s = Solution()
s.minimumSubarrayLength(nums, k)
