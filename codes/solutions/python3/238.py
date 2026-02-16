from functools import reduce
from typing import List


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m, res = 1, []
        for i in range(len(nums)):
            res.append(m)
            m *= nums[i]
        m = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= m
            m *= nums[i]
        return res


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        prefix_prod = [1] * (len(nums) + 1)
        for i in range(0, len(nums)):
            prefix_prod[i + 1] = prefix_prod[i] * nums[i]
        prod_ = 1
        for j in range(len(nums) - 1, -1, -1):
            prod[j] = prefix_prod[j] * prod_
            prod_ *= nums[j]
        return prod


x = Solution2().productExceptSelf( [-1,1,0,-3,3])
print(x)
