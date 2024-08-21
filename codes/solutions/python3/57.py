from bisect import *


class Solution:
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     new, i = [], 0
    #     for i, it in enumerate(intervals):
    #         if newInterval[1] < it[0]:
    #             i -= 1
    #             break
    #         elif it[1] < newInterval[0]:
    #             new += it,
    #         else:
    #             newInterval[0], newInterval[1] = min(it[0], newInterval[0]), max(it[1], newInterval[1])
    #     return new + [newInterval] + intervals[i + 1:]
    def insert2(self, intervals, new_interval):
        insort_left(intervals, new_interval, key=lambda it: it[0])

        s = []
        for i in intervals:
            if s and s[-1][1] >= i[0]:
                s[-1][1] = max(s[-1][1], i[1])
            else:
                s.append(i)
        return intervals


import bisect

print(bisect.__file__)
s = Solution()
s.insert2([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [3, 8])
