from typing import List


class Solution:
    def trap(self, height):
        res, left, l, r = 0, {}, 0, 0
        for i, h in enumerate(height):
            left[i] = l
            if h > l:
                l = h
        for i in range(len(height) - 1, -1, -1):
            roof = min(left[i], r)
            if roof > height[i]:
                res += roof - height[i]
            if height[i] > r:
                r = height[i]
        return res

    def trap2(self, height):
        left = [-1] * len(height)
        for i in range(len(height)):
            left[i] = max(left[i - 1], height[i])
        right = [-1] * len(height)
        for i in range(len(height) - 1, -1, -1):
            right[i] = max(right[(i + 1)%len(height)], height[i])

        return sum([min(left[i], right[i]) - height[i] for i in range(len(height))])

class Solution1:
    def trap(self, height: List[int]) -> int:
        max_water = 0
        i, j = 0, len(height) - 1
        left = [-1] * len(height)
        left[0] = height[0]
        right = [-1] * len(height)
        left[0] = height[0]
        right[-1] = height[-1]
        for i in range(1, len(height)):
            left[i] = max(left[i - 1], height[i])
        for i in range(len(height)-2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        return sum(min(left[i], right[i]) - height[i] for i in range(len(height)))

heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = Solution1()
assert s.trap(heights) == s.trap(heights)
