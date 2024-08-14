from collections import Counter
from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        arr = sorted(deliciousness)

        def count_pair_with_sum(s):
            pairs, c = Counter(), 0
            for x in arr:
                if s - x in pairs:
                    c += pairs[s - x]
                pairs[x] += 1
            return c % (10 ** 9 + 7)

        return sum(count_pair_with_sum(2 ** i) for i in range(22))


print(countPairs([149, 107, 1, 63, 0, 1, 6867, 1325, 5611, 2581, 39, 89, 46, 18, 12, 20, 22, 234]))
