import heapq
from typing import List
from collections import defaultdict, OrderedDict


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lake_day_rain_mp = defaultdict(list)
        filled_lakes = OrderedDict()
        ans = [-1] * len(rains)
        heap = []
        for d, l in enumerate(rains):
            if l > 0:
                lake_day_rain_mp[l].append(d)

        for d, l in enumerate(rains):
            if l > 0:
                if l in filled_lakes:
                    return []
                else:
                    next_days = lake_day_rain_mp[l]
                    next_days.pop(0)
                    if next_days:
                        heapq.heappush(heap, (next_days[0], l))
                    filled_lakes[l] = True
            else:
                if filled_lakes:
                    if heap:
                        _, lake_to_dry = heapq.heappop(heap)
                    else:
                        lake_to_dry = next(iter(filled_lakes))
                    ans[d] = lake_to_dry
                    filled_lakes.pop(lake_to_dry)
                else:
                    ans[d] = 1
        return ans


rains = [1, 0, 2, 0]
print(Solution().avoidFlood(rains))
