import collections


class Solution:
    def subarraysWithKDistinct(self, A, K):
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        count = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if count[A[j]] == 0: K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0: K += 1
                i += 1
            res += j - i + 1
        return res

    def substringWithKdistinct2(self, s, k):
        start = 0
        freq = {}
        mx = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            while len(freq) > k:
                freq[s[i]] = freq.get(s[start]) - 1
                if freq[s[i]] == 0:
                    freq.pop(s[i])
                start += 1
            mx = max(mx, i - start + 1)
        return mx
# Input: s = "ecebee", k = 2
# Output: 3("ece")

x=Solution().substringWithKdistinct2('ecebee',2)
print(x)