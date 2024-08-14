import functools
from typing import List


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter as ct
        return [k for (k, v) in ct(nums).most_common(k)]

    def topKFrequent2(self, nums, k):
        from collections import Counter, OrderedDict
        class OrderedCounter(Counter, OrderedDict):
            pass

        import heapq
        heap = []
        it = iter(OrderedCounter(nums).items())
        for _ in range(k):
            i, p = next(it)
            heapq.heappush(heap, (p, i))
        while True:
            try:
                i, p = next(it)
            except StopIteration:
                break
            if p > heap[0][0]:
                heap[0] = (p, i)
                heapq.heappop(heap)
                heapq.heappush(heap, (p, i))
        res = []
        while heap:
            _, i = heapq.heappop(heap)
            res.append(i)
        return res


def topKFrequent(words: List[str], k: int) -> List[str]:
    from collections import Counter, OrderedDict
    import heapq
    class OrderedCounter(Counter, OrderedDict):
        pass

    words.sort(reverse=True)
    counter = OrderedCounter(words)  # O(n)
    h = list(zip(counter.values(), counter.keys()))
    heap = h[:k]
    heapq.heapify(heap)
    for i in range(k, len(h)):
        if heap[0][0] < h[i][0] or (heap[0][0] == h[i][0] and heap[0][1] > h[i][1]):
            heapq.heappop(heap)
            heapq.heappush(heap, h[i])

    def cmp(x, y):
        if x[0] == y[0]:
            return -1 if x[1] < y[1] else 1
        return -1 if x[0] > y[0] else 1

    heap = sorted(heap, key=functools.cmp_to_key(cmp))
    return list(map(lambda x: x[1], heap))


nums = ["aaa", "aa", "a"]
k = 2
print(topKFrequent(nums, k))
