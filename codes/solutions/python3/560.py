# class Solution:
#     def subarraySum(self, nums, k):
#         sums, res, sm = {}, 0, 0
#         for i in range(len(nums)):
#             sums[sm], sm = sm in sums and sums[sm] + 1 or 1, sm + nums[i]
#             if sm - k in sums: res += sums[sm - k]
#         return res
#
#     def subarrayswithSumK(self, nums, k):
#         d = {0: -1}
#         cur_sum = 0
#         res = []
#         for i, x in enumerate(nums):
#             cur_sum += x
#             if cur_sum - k in d:
#                 res.append(nums[d[cur_sum - k] + 1:i + 1])
#             d[cur_sum] = i
#         print(res)
#         return res
#
#
# nums = [1, 2, 3]
# k = 3
# Solution().subarrayswithSumK(nums, k)
import sys

A = [1, 6, 2]
B = [3, 2, 5]
X = 2
Y = 1
dp = [[sys.maxsize, sys.maxsize] for _ in range(len(A))]
dp[0] = [A[0], B[0]]
for i in range(1, len(A)):
    dp[i][0] = min(dp[i - 1][0], dp[i - 1][1] + Y) + A[i]
    dp[i][1] = min(dp[i - 1][1], dp[i - 1][0] + X) + B[i]
print(min(dp[-1]))
