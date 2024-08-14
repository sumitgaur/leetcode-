from typing import List


class Solution:
    def minAvailableDuration(self, s1: List[List[int]], s2: List[List[int]], d: int) -> List[int]:
        s2.sort()
        j = 0
        for s, e in sorted(s1):
            while j < len(s2) - 1 and s2[j][1] < s:
                j += 1
            if s2[j][0] <= e:
                l, r = max(s, s2[j][0]), min(e, s2[j][1])
                if r - l >= d:
                    return [l, l + d]

    def minAvailableDuration2(self, s1, s2, d):
        t1, t2 = 0, 0
        while t1 < len(s1) and t2 < len(s2):
            ox, oy = max(s1[t1][0], s2[t2][0]), min(s1[t1][1], s2[t2][1])  # overlap
            if oy - ox >= d:
                return [ox, ox + d]
            elif s1[t1][1] > s2[t2][1]:
                t2 += 1
            else:
                t1 += 1
        return []


slots1 = [[10, 50], [60, 120], [140, 210]]
slots2 = [[0, 15], [60, 70]]
duration = 5
print(Solution().minAvailableDuration2(slots1, slots2, duration))
