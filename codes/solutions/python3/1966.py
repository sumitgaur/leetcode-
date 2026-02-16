import sys


def binarySearchableNumbers(nums):
    if not nums: return 0
    max_left = [nums[0]] * len(nums)
    min_right = [nums[-1]] * len(nums)
    # find max(Aj) j<i
    for i in range(1, len(nums)):
        max_left[i] = max(nums[i], max_left[i - 1])

    for i in range(len(nums) - 2, -1, -1):
        min_right[i] = min(nums[i], min_right[i + 1])
    bsearchable_count = 0
    for i in range(len(nums)):
        if max_left[i] <= nums[i] and nums[i] <=  min_right[i]:
            bsearchable_count += 1
    return bsearchable_count


nums = []
print(binarySearchableNumbers(nums))
