from collections import Counter


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mp = Counter()
        count = len(s)
        for ch in s:
            count += mp[ch]
            mp[ch] += 1
        return count

s = 'aba'
print(Solution().numberOfSubstrings(s))