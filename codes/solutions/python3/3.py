class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mx, start, chars = 0, 0, {}
        for i in range(len(s)):
            if s[i] in chars and start <= chars[s[i]]:
                start = chars[s[i]] + 1
            else:
                mx = max(mx, i - start + 1)
            chars[s[i]] = i
        return mx

    def lengthOfLongestSubstring2(self, s):
        start = 0
        mx = 0
        best_i = best_e = 0
        seen = {}
        for i in range(len(s)):
            if s[i] in seen and start <= seen[s[i]]:
                start = seen[s[i]] + 1
            else:
                if mx < i - start + 1:
                    mx = i - start + 1
                    best_i = start
                    best_e = i
            seen[s[i]] = i
        return s[best_i:best_e + 1]

        # Input: "abcdbcbb"
# Output: 3
# Explanation: "abc"

print(Solution().lengthOfLongestSubstring2('abcdbefb'))