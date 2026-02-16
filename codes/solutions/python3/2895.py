from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        j = 0
        min_time_to_complete = 0
        for i in range(0, len(tasks), 4):
            min_time_to_complete = max(
                min_time_to_complete, max(processorTime[j] + tasks[i])
            )
            j += 1
        return min_time_to_complete

obj = Solution()

obj.minProcessingTime([8,10],[2,2,3,1,8,7,4,5])