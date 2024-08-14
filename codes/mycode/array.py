import sys
from builtins import object, enumerate
from collections import deque, defaultdict
from typing import List
import heapq


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    hq, res = [], []
    for i in range(k):
        hq.append((-nums[i], i))
    heapq.heapify(hq)
    for i in range(k, len(nums)):
        res.append(-hq[0][0])
        hq.remove((-nums[i - k], i - k))
        hq.append((-nums[i], i))
        heapq.heapify(hq)
    res.append(-hq[0][0])
    return res


def maxSlidingWindow1(nums: List[int], k: int) -> List[int]:
    d = deque()
    out = []
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()
        d.append(i)
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            out.append(nums[d[0]])
    return out


def candy(ratings: List[int]) -> int:
    dp = [1] * len(ratings)
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            dp[i] = dp[i - 1] + 1

    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and dp[i] <= dp[i + 1]:
            dp[i] = dp[i + 1] + 1
    return sum(dp)


def maxPairs(skillLevel, minDiff):
    skillLevel = sorted(skillLevel)
    pairs = set()
    p_count = 0
    for j in range(len(skillLevel) - 1, -1, -1):
        i = j - 1
        while i > 0 and skillLevel[j] - skillLevel[i] < minDiff:
            i -= 1
        if i >= 0 and (i not in pairs and j not in pairs):
            pairs |= {i, j}
            p_count += 1

    return p_count


def track_switching(obstacles: List[int]) -> int:
    all_tracks = [1, 2, 3]

    def do(cur_track, i):
        if i < len(obstacles):
            if obstacles[i] == cur_track:
                a, b = [i for i in all_tracks if i != cur_track]
                return min(do(a, i + 1) + 1, do(b, i + 1) + 1)
            return do(cur_track, i + 1)
        return 0

    return do(2, 0)


def canCompleteCircuit(gas, cost):
    for i in range(len(gas)):
        cur_fuel = 0
        j, traversed = i, 0
        while cur_fuel + gas[j] >= cost[j]:
            traversed += 1
            cur_fuel += gas[j] - cost[j]
            j = (j + 1) % len(gas)
            if traversed == len(gas):
                return i
    return -1


def exclusiveTime(n: int, logs: List[str]) -> List[int]:
    top = [logs[0].split(":")[0]]
    ex_t = defaultdict(int)
    prev_time = 0
    for i, log in enumerate(logs):
        f_id, start_or_end, ts = log.split(":")
        ts = int(ts)
        if start_or_end == "start":
            ex_t[top[-1]] += ts - prev_time
            prev_time = ts
            top.append(f_id)
        else:
            top.pop()
            ex_t[f_id] += ts - prev_time + 1
            prev_time = ts + 1

    return [ex_t[x] for x in sorted(ex_t)]


def minMeetingRooms(A):
    in_ = [A[i][0] for i in range(len(A))]
    out = [-A[i][1] for i in range(len(A))]
    seq = sorted(in_ + out, key=abs)
    rooms = min_rooms = i = 0
    while i < len(seq):
        if i + 1 < len(seq) and seq[i] > 0 and seq[i] == -seq[i + 1]:
            i += 2
        rooms += 1 if seq[i] >= 0 else -1
        min_rooms = max(min_rooms, rooms)
        i += 1
    return min_rooms


def pairs(k, arr):
    """
    find pairs with diff
    :param k:
    :param arr:
    :return:
    """
    mp = set()
    pairs = 0
    for x in arr:
        pairs += sum((x - k in mp, x + k in mp))
        mp.add(x)
    return pairs


# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    st = []
    bal = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in [')', '}', ']']:
            if st and st.pop() != bal[c]:
                return "NO"
        else:
            st.append(c)
    return "YES"


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    counts = [[0, []] for _ in range(101)]
    for i, x in enumerate(nums):
        counts[x][0] += 1
        counts[x][1].append(i)
    res = [0] * len(nums)
    small_elts = 0
    for c, indices in counts:
        for i in indices:
            res[i] = small_elts
        small_elts += c
    return res


def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[1, -1] for _ in range(len(nums))]
    for i, x in enumerate(nums):
        j = i - 1
        while j >= 0:
            if x % nums[j] == 0:
                if dp[j][0] + 1 > dp[i][0]:
                    dp[i] = [dp[j][0] + 1, j]
            j -= 1
    i, _ = max(enumerate(dp), key=lambda x: x[1][0])
    res = []
    while i != -1:
        res.append(nums[i])
        i = dp[i][1]
    return res[::-1]


def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    return sorted(arr1, key=lambda x: arr2.index(x) if x in arr2 else arr1.index(x))


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
print(relativeSortArray(arr1, arr2))


def cube_root(num):
    l, r = 0, num // 2
    while l <= r:
        m = (l + r) // 2
        cube = m * m * m
        if cube == num:
            return m
        elif cube > num:
            r = m - 1
        else:
            l = m + 1
    return None


# largestDivisibleSubset([1, 4, 7, 8, 16])
# smallerNumbersThanCurrent([8, 1, 2, 2, 3])
# pairs(2, [1, 5, 3, 4, 2])

# logs = ["0:start:0", "1:start:5", "2:start:6", "3:start:9", "4:start:11", "5:start:12", "6:start:14", "7:start:15",
#         "1:start:24", "1:end:29", "7:end:34", "6:end:37", "5:end:39", "4:end:40", "3:end:45", "0:start:49", "0:end:54",
#         "5:start:55", "5:end:59", "4:start:63", "4:end:66", "2:start:69", "2:end:70", "2:start:74", "6:start:78",
#         "0:start:79", "0:end:80", "6:end:85", "1:start:89", "1:end:93", "2:end:96", "2:end:100", "1:end:102",
#         "2:start:105", "2:end:109", "0:end:114"]
# exclusiveTime(2, logs)
# gas = [ 1, 2, 3, 4, 5 ]
# cost = [ 3, 4, 5, 1, 2 ]
#
# print(canCompleteCircuit(gas, cost))
# print(track_switching([2, 1, 2, 3, 2]))
# nums = [3, 4, 5, 2, 1, 1]
# print(maxPairs(nums, 3))
# nums = [1, 3, 1, 2, 0, 5]
# k = 3
# print(maxSlidingWindow1(nums, k))

# A = [
#     [7, 10],
#     [4, 19],
#     [19, 26],
#     [14, 16],
#     [13, 18],
#     [16, 21]
# ]
# minMeetingRooms(A)
# 0 1 0 0 1
# 0 1 1 0 0
# 0 1 0 0 1
# 0 0 1 0 1
# 3,2,1 max = 3

def max_island_area(mat):
    visited, mx = {}, 0,

    def dfs(mat, i, j, area):
        if 0 <= i < len(mat) and 0 <= j < len(mat[0]) and (i, j) not in visited and mat[i][j] == 1:
            visited[(i, j)] = True
            area[0] = area[0] + 1
            for u, v in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                dfs(mat, i + u, v + j, area)

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (i, j) not in visited and mat[i][j] == 1:
                area = [0]
                dfs(mat, i, j, area)
                mx = max(mx, area[0])
    return mx


def solve(A):
    def do(A):
        if len(A) == 1:
            return (A[0], A[0])
        if len(A) == 2:
            return (A[0], A[1]) if A[0] < A[1] else (A[1], A[0])
        m = len(A) // 2
        x1, y1 = do(A[:m])
        print(x1, y1)
        x2, y2 = do(A[m:])
        print(x2, y2)
        return (min(x1, x2), max(y1, y2))

    x, y = do(A)
    return x + y


A = [-2, 1, -4, 5, 3]
solve(A)
# [0, 1, 1, 0, 0],
# [0, 1 ,0, 0, 1],
# [0, 0, 1, 0, 1]
# ]
# mat = [[0, 1],
#        [1, 0]]
# print(max_island(mat))
