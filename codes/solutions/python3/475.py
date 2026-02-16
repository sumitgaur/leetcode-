from typing import List


class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        r = 0
        for h in houses:
            ind = bisect.bisect_left(heaters, h)
            if ind == len(heaters):
                r = max(r, h - heaters[-1])
            elif ind == 0:
                r = max(r, heaters[0] - h)
            else:
                r = max(r, min(heaters[ind] - h, h - heaters[ind - 1]))
        return r

from collections import defaultdict
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def merge_sorted_arrays(arr1, arr2):
            merged = []
            i = 0  # Pointer for arr1
            j = 0  # Pointer for arr2

            # Traverse both arrays and append the smaller element
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    merged.append([arr1[i], 0])
                    i += 1
                else:
                    merged.append([arr2[j], 1])
                    j += 1

            # Append remaining elements from arr1 (if any)
            while i < len(arr1):
                merged.append([arr1[i], 0])
                i += 1

            # Append remaining elements from arr2 (if any)
            while j < len(arr2):
                merged.append([arr2[j], 1])
                j += 1

            return merged

        houses.sort()
        heaters.sort()
        houses_heaters = merge_sorted_arrays(houses, heaters)

        min_dist_heater = defaultdict(lambda: float("inf"))

        def heater_dist(houses_heaters, min_dist_heater):
            near_heater = None
            for h in houses_heaters:
                if h[1] == 0:  # house found
                    if near_heater:
                        min_dist_heater[h[0]] = min(min_dist_heater[h[0]], abs(h[0] - near_heater))
                else:  # heater found
                    near_heater = h[0]

        heater_dist(houses_heaters, min_dist_heater)
        heater_dist(houses_heaters[::-1], min_dist_heater)
        return max(min_dist_heater.values())

houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]

print(Solution().findRadius(houses,heaters))

