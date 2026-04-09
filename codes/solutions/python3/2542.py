import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def pick(i, k, cur_sum, min_):
            if k == 0:
                return cur_sum * min_
            if i < len(nums1):
                return max(
                    pick(
                        i + 1, k - 1, cur_sum + nums1[i], min(min_, nums2[i])
                    ),  # pick ith elt
                    pick(i + 1, k, cur_sum, min_),  # skip ith elt
                )
            return -1

        return pick(0, k, 0, float("inf"))

    def maxScore_(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        heap = []
        res = 0
        cur_sum = 0
        for n2, n1 in pairs:
            if len(heap) == k:
                res = max(cur_sum * n2, res)
            if len(heap) < k:
                heapq.heappush(heap, n1)
                cur_sum += n1
            else:
                cur_sum -= heapq.heappop(heap)
        return res
