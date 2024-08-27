from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        line = [0] * 101
        era_start = 1950
        for by, dy in logs:
            line[by - era_start] += 1
            line[dy - era_start] -= 1
        max_count = 0
        max_count_year = None
        pop_count = 0
        for i, c in enumerate(line):
            pop_count += c
            if pop_count > max_count:
                max_count_year = era_start + i
                max_count = pop_count
        return max_count_year


logs = [[1982, 1998], [2013, 2042], [2010, 2035], [2022, 2050], [2047, 2048]]

print(Solution().maximumPopulation(logs))

