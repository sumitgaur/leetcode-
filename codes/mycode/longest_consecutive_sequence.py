# Longest Consecutive Sequence
# Input:
# nums = [100,4,200,1,3,2]
#
# Output:
# 4

def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    cur_len = 0
    max_len = 0
    start = None
    for x in nums_set:
        if x - 1 not in nums_set:
            start = x
            cur_len = 0
            while start in nums_set:
                cur_len += 1
                start = start + 1
            max_len = max(max_len, cur_len)
    return max_len


nums =[1,2,3,4]
print(longest_consecutive_sequence(nums))


