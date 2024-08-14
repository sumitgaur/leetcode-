from collections import Counter


class Solution:
    def minWindow(self, s, t):
        cnt_s, cnt_t, n, left, r = {}, {}, len(s), set(t), -1
        for c in t:
            cnt_t[c] = cnt_t.get(c, 0) + 1
        L = l = 0
        while left:
            r += 1
            if r >= n:
                return ""
            cnt_s[s[r]] = cnt_s.get(s[r], 0) + 1
            if s[r] in cnt_t and cnt_s[s[r]] == cnt_t[s[r]]:
                left.discard(s[r])
        R = r
        cnt_s[s[r]] -= 1
        while l < r < n:
            cnt_s[s[r]] = cnt_s.get(s[r], 0) + 1
            while s[l] not in cnt_t or cnt_s[s[l]] > cnt_t[s[l]]:
                cnt_s[s[l]] -= 1
                l += 1
            if r - l < R - L:
                L, R = l, r
            r += 1   
        return s[L: R + 1]

    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t)  # counter for t to check with
        window = Counter()  # sliding window
        ans = ""  # answer
        last = 0  # last index in our window
        for i, char in enumerate(s):
            window[char] = window.get(char, 0) + 1  # add this character to our window
            while window >= tCounter:  # while we have all the necessary characters in our window
                if ans == "" or i - last < len(ans):  # if the answer is better than our last one
                    ans = s[last:i + 1]  # update ans
                window[s[last]] -= 1  # remove the last element from our counter
                last += 1  # move the last index forward
        return ans  # return answer