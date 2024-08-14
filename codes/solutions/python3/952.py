# class Solution:
#     def largestComponentSize(self, A):
#         def find(i):
#             return i if i == parent[i] else find(parent[i])
#
#         def prime_factors(n):
#             res = set()
#             while n % 2 == 0:
#                 res.add(2)
#                 n //= 2
#             for i in range(3, int(n ** 0.5) + 1, 2):
#                 while n % i == 0:
#                     res.add(i)
#                     n //= i
#             if n > 2:
#                 res.add(n)
#             return res
#
#         parent, dic = list(range(len(A))), {}
#         for i, n in enumerate(A):
#             for p in prime_factors(n):
#                 if p in dic:
#                     parent[find(i)] = find(dic[p])
#                 dic[p] = i
#         for i, x in enumerate(parent):
#             parent[i] = find(x)
#         return max(collections.Counter(parent).values())
#
from typing import List


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        p = list(range(n))
        size = [1] * n

        def find(u):
            while p[u] != u:
                u = p[u]
            return u

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu != pv:
                if size[pu] > size[pv]:
                    p[pv] = pu
                    size[p[pv]] = size[pu] + size[pv]
                else:
                    p[pu] = pv
                    size[p[pu]] = size[pu] + size[pv]

        def prime_factors(n):
            res = set()
            while n % 2 == 0:
                res.add(2)
                n //= 2
            for i in range(3, int(n ** 0.5) + 1, 2):
                while n % i == 0:
                    res.add(i)
                    n //= i
            if n > 2:
                res.add(n)
            return res
        d = {}
        for i in range(n):
            for pf in prime_factors(nums[i]):
                if pf in d:
                    union(i, d[pf])
                d[pf] = i

        return max(size)


nums = [20,50,9,63]
print(Solution().largestComponentSize(nums))
