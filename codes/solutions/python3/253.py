# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x.start)
        heap, time, rooms = [], 0, 0
        for intr in intervals:
            while heap and heap[0] <= intr.start:
                heapq.heappop(heap)
            heapq.heappush(heap, intr.end)
            if len(heap) > rooms:
                rooms += 1
        return rooms

    def minMeetingRooms1(self, intervals):
        in_out_time = []
        for x, y in intervals:
            in_out_time.append(x)
            in_out_time.append(-y)
        in_out_time.sort(key=lambda x: abs(x))
        rooms_req = 0
        min_rooms = 0
        for x in in_out_time:
            if x >= 0:
                rooms_req += 1
            else:
                rooms_req -= 1
            min_rooms = max(min_rooms, rooms_req)
        return min_rooms


meetings = [[0, 30], [5, 10], [15, 20]]
print(Solution().minMeetingRooms1(meetings))
