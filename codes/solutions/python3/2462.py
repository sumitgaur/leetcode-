import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        i = candidates
        j = max(candidates, len(costs) - candidates)
        start_heap = costs[:i]
        end_heap = costs[j:]
        heapq.heapify(start_heap)
        heapq.heapify(end_heap)
        res = 0
        for _ in range(k):
            if start_heap[0] <= end_heap[0]:
                res += heapq.heappop(start_heap)
                i += 1
                heapq.heappush(start_heap, costs[i])
            else:
                res += heapq.heappop(end_heap)
                j -= 1
                heapq.heappush(end_heap, costs[j])
        return res


costs = [1, 2, 4, 1]
k = 3
candidates = 3

print(Solution().totalCost(costs, k, candidates))
