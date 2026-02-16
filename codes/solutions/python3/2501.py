class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        hash_set = set(nums)
        visited = set()
        nums.sort()
        mx = -1
        for x in nums:
            c = 0
            while x not in visited and x in hash_set:
                visited.add(x)
                x *= x
                c += 1
            mx = max(mx, c)
        return mx if mx >= 2 else -1
