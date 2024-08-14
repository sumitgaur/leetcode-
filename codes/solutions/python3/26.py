class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        return n - len([nums.pop(i) for i in range(n -1, 0, -1) if nums[i] == nums[i - 1]])https://www.amazon.in/boAt-Bluetooth-Signature-Multi-Connectivity-Premium-Black/dp/B0C36ZDJPV?th=1