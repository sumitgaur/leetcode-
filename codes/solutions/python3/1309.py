class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        res = []
        while i >= 0:
            if s[i] == '#':
                res += chr(ord('a') + int(s[i - 2:i]) - 1)
                i -= 3
            else:
                res += chr(ord('a') + int(s[i]) - 1)
                i -= 1
        return ''.join(res[::-1])


s = "1326#"
x = Solution().freqAlphabets(s)
print(x)
