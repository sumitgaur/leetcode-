class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


class Solution2:

    def reverseWords(self, s: str) -> str:
        def _reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        s = s.strip()
        s = list(s[::-1])
        i, j = 0, 0
        while j < len(s):
            if s[j] == ' ':
                _reverse(s, i, j - 1)
                i = j + 1
            j += 1
        _reverse(s, i, j - 1)
        return ''.join(s)


x = Solution2().reverseWords("  hello world  ")
print(x)
