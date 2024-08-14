from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: abs(x[0] - x[1]))
        a = b = 0
        N = len(costs) // 2
        c = 0
        for c1, c2 in costs[::-1]:
            if c1 <= c2 and a < N or b >= N:
                c += c1
                a += 1
            else:
                c += c2
                b += 1
        return c


class Solution1:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        city_a_sorted = sorted(enumerate(costs), key=lambda c: c[1][0])
        city_b_sorted = sorted(enumerate(costs), key=lambda c: c[1][1])
        t1 = t2 = 0
        n = len(costs) / 2
        city_a_cost = set()
        city_b_cost = set()
        while len(city_a_cost) < n or len(city_b_cost) < n:
            while city_a_sorted[t1][0] in city_b_cost:
                t1 += 1
            city_a_cost.add(city_a_sorted[t1][0])
            t1 += 1
            while city_b_sorted[t2][0] in city_a_cost:
                t2 += 1
            city_b_cost.add(city_b_sorted[t2][0])
            t2 += 1
        print(city_a_sorted)
        print(city_b_sorted)
        print(city_a_cost, city_b_cost)
        return sum(costs[i][0] for i in city_a_cost) + sum(costs[i][1] for i in city_b_cost)


costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
Solution1().twoCitySchedCost(costs)
