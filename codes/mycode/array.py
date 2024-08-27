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
    st, pairs = [], {'(': ')', '{': '}', '[': ']'}
    for c in s:
        if c in pairs:
            st.append(c)
        else:
            if not st or pairs[st.pop()] != c:
                return False
    return st == []


print(isBalanced("{()"))


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


def serve_customers(arr, initial_amt):
    max_serve = 0
    l = 0
    amt = initial_amt
    for r in range(len(arr)):
        amt += arr[r]
        while l < len(arr) and amt < 0:
            amt -= arr[l]
            l += 1
        max_serve = max(max_serve, r - l + 1)
    return max_serve


# print(serve_customers.__name__)
# transactions = [-5, 3, -2, 4, -1]
#
# print(serve_customers(transactions, 1))
# A = [-2, 1, -4, 5, 3]
# solve(A)
# [0, 1, 1, 0, 0],
# [0, 1 ,0, 0, 1],
# [0, 0, 1, 0, 1]
# ]
# mat = [[0, 1],
#        [1, 0]]
# print(max_island(mat))

# An stone array is given.
# A mouse is on index 0 initially, he starts jumping towards right.
# Score of a jump is = (len of jump * value of stone mouse is jumping on to)
# for eg : Score of jump from i to j, score would be = (j-i)*stone[j]
# Mouse can make any number of jumps, find what is the maximum score that can be achieved.
#
# ex
# 3 5 4 7 2 12 8 10 1
#
# ex: 3 to 12 (512) + 12 to 10 (210) + 10 to 1 (1*1) = 81
def collect_stones(arr):
    dp = [0] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            dp[i] = max(dp[i], dp[j] + (i - j) * arr[i])
    return max(dp)


# stones = [3, 5, 4, 7, 2, 12, 8, 10, 1]
# print(collect_stones(stones))

# Assume there is a street of blocks and each block has apartment available to rent out.
# You're hunting for an apartment in that street and each block has a set of amenities that you want
# to have easy access to from your new home. Each block has zero or more amenities.
# How would you pick the block to live in such that the farthest distance to any amenity in your list is minimized?
def find_closest_apartment(blocks, reqs):
    block_dist = [{req: sys.maxsize for req in reqs} for _ in range(len(blocks))]
    for i in range(len(blocks)):
        for req in reqs:
            if blocks[i][req]: block_dist[i][req] = 0

    for i in range(1, len(blocks)):
        for req in reqs:
            block_dist[i][req] = min(block_dist[i][req], block_dist[i - 1][req] + 1)

    for i in range(len(blocks) - 2, -1, -1):
        for req in reqs:
            block_dist[i][req] = min(block_dist[i][req], block_dist[i + 1][req] + 1)
    best_apartment = None
    best_apartment_dist = sys.maxsize
    for i in range(len(blocks)):
        if max(block_dist[i].values()) < best_apartment_dist:
            best_apartment_dist = max(block_dist[i].values())
            best_apartment = i
    return best_apartment


# blocks = [{
#     "gym": False,
#     "school": True,
#     "store": False
# }, {
#     "gym": True,
#     "school": False,
#     "store": False
# }, {
#     "gym": True,
#     "school": True,
#     "store": False
# }, {
#     "gym": False,
#     "school": True,
#     "store": False
# }, {
#     "gym": False,
#     "school": True,
#     "store": True
# }]
#
# reqs = ["gym", "school"]
# print(find_closest_apartment(blocks, reqs))


# You are given 2 arrays representing integer locations of stores and houses
# (each location in this problem is one-dementional). For each house, find the store closest to it.
# Return an integer array result where result[i] should denote the
# location of the store closest to the i-th house. If many stores are equidistant
# from a particular house, choose the store with the smallest numerical location.
# Note that there may be multiple stores and houses at the same location.
# Input: houses = [5, 10, 17], stores = [1, 5, 20, 11, 16]
# Output: [5, 11, 16]

def closest_stores(houses, stores):
    normalized_points = houses + list(map(lambda x: -x, stores))
    normalized_points = sorted(normalized_points, key=lambda x: abs(x))
    dp = [None] * len(normalized_points)
    prev_store = None
    for i, point in enumerate(normalized_points):
        if point > 0:
            dp[i] = prev_store
        else:
            prev_store = abs(point)
    for i in range(len(normalized_points) - 1, -1, -1):
        if normalized_points[i] > 0:
            if abs(normalized_points[i] - dp[i]) > abs(normalized_points[i] - prev_store):
                dp[i] = prev_store
        else:
            prev_store = abs(normalized_points[i])
    return [p for p in dp if p]


#
# houses = [5, 10, 17]
# stores = [1, 5, 20, 11, 16]
# print(closest_stores(houses, stores))


# count rectangles || to x and y axis
def count_rectangles(points):
    points_set = set((x, y) for x, y in points)
    count = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 != x2 and y1 != y2:
                if (x1, y2) in points_set and (x2, y1) in points_set:
                    count += 1
    return count // 2


# points = [(1, 1), (1, 3), (3, 1), (3, 3), (2, 2)]
# print(count_rectangles(points))

# Problem: Write a function to determine if it's possible to make a single vertical cut through a rectangular cake with non-overlapping toppings such that:
#
# The cut does not intersect or destroy any of the toppings.
# After the cut, both resulting pieces of the cake each contain at least one topping.
#
# List of toppings with their positions [topping (start_x, end_x, start_y, end_y) ]
# Output:
# True/False
# Example:
# Input :
# a (0,6,0, 1); b (7,8,0,4); c(0, 1,2,4) ;
def cake_cut_vertical(toppings):
    x_ranges = [(x, y) for x, y, _, _ in toppings]
    x_ranges.sort(key=lambda x: (x[0], x[1]))
    prev_end = x_ranges[0][1]
    for x1, x2 in x_ranges[1:]:
        if x1 > prev_end:
            return prev_end
        prev_end = max(prev_end, x2)
    return False


# toppings = [(0, 6, 0, 1), (7, 8, 0, 4), (0, 1, 2, 4)]
# print(cake_cut_vertical(toppings))

# Given on-call rotation schedule for multiple people by: their name, start time and end time of the rotation:
#
# Abby 1 10
# Ben 5 7
# Carla 6 12
# David 15 17
#
# Your goal is to return rotation table without overlapping periods representing who is on call during that time. Return "Start time", "End time" and list of on-call people:
#
# 1 5 Abby
# 5 6 Abby, Ben
# 6 7 Abby, Ben, Carla
# 7 10 Abby, Carla
# 10 12 Carla
# 15 17 David


def on_call(logs):
    from sortedcontainers import SortedDict
    line = SortedDict()
    for name, s, e in logs:
        line[s] = name
        line[e] = name
    line = list(line.items())
    visited = {line[0][1]}
    res = []
    st = line[0][0]
    for time, name in line[1:]:
        if visited:
            res.append([st, time, list(visited)])
        if name in visited:
            visited.remove(name)
        else:
            visited.add(name)
        st = time
    return res


logs = [['Abby', 1, 10], ['Ben', 5, 7], ['Carla', 6, 12], ['David', 15, 17]]
print(on_call(logs))
