class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans

    def largestRectangleArea2(self, heights):
        def next_min(arr):
            st = []
            nexts = [-1] * len(arr)
            for i in range(len(arr)):
                while st and arr[i] < arr[st[-1]]:
                    nexts[st.pop()] = i
                st.append(i)
            return nexts

        prev, next = next_min(heights[::-1]), next_min(heights)
        prev, next = [len(heights) - 1 - i if i != -1 else i for i in prev][::-1], list(map(
            lambda x: x if x != -1 else len(heights), next))
        res = 0
        for i in range(len(heights)):
            res = max(res, heights[i] * (next[i] - prev[i] - 1))

        return res


heights = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea2(heights))
