from typing import List


class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res, stack = [], [nums[0] if nums else None, None]
        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == num - 1: stack[1] = num
            if i > 0 and nums[i-1] != num - 1: res, stack[0], stack[1] = res + ["->".join(str(q) for q in stack if q != None)], num, None
            if i == len(nums) - 1: res.append("->".join(str(q) for q in stack if q != None))
        return res
    def summaryRanges2(self, nums: List[int]) -> List[str]:
        ranges,i=[],0
        while i <len(nums):
            elt=nums[i]
            while (i+1)<len(nums) and nums[i+1]==nums[i]+1:
                i+=1
            if elt!=nums[i]:
                ranges.append(f"{elt}->{nums[i]}")
            else:
                ranges.append(f"{elt}")
            i+=1
        return ranges

print(Solution().summaryRanges2([0,1,2,4,5,7]))