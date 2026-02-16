# You have a dictionary / map:
#
# key → value
#
#
# You need to support:
#
# put(key, value)
#
# delete(key)
#
# get max value at any time
import heapq
from typing import Optional

from sortedcontainers import SortedDict


class HeapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


class DictionaryWithMax:
    def __init__(self):
        self._dict = {}
        self.max_values_heap = []

    def get(self, key: str) -> Optional[int]:  # O(1)
        return self._dict.get(key, None)

    def put(self, key: str, value: int):  # O(lgn)
        node = HeapNode(key, value)
        self._dict[key] = node
        heapq.heappush(self.max_values_heap, node)

    def delete(self, key: str):  # O(1)
        self._dict.pop(key, None)

    def max(self):  # O(lgn) Lazy deletion
        while self.max_values_heap and self.max_values_heap[0].key not in self._dict:
            heapq.heappop(self.max_values_heap)
        return self.max_values_heap and self.max_values_heap[0].value


class DictionaryWithMax2:
    def __init__(self):
        self.original_dict = {}
        self.values_dict = SortedDict()

    def get(self, key: str) -> Optional[int]:  # O(1)
        return self.original_dict.get(key, None)

    def put(self, key: str, value: int):  # O(lgn)

        self.original_dict[key] = value
        if value in self.values_dict:
            self.values_dict[value].add(key)
        else:
            self.values_dict[value] = {key}

    def delete(self, key: str):  # O(1)
        v = self.original_dict.pop(key, None)
        if v is not None:
            self.values_dict[v].remove(key)
            if not self.values_dict.get(v):
                self.values_dict.pop(v)
        return v

    def max(self):  # O(lgn) Lazy deletion
        return self.values_dict.peekitem(-1)


#
# a->1
# b->2
# c->3
# max = 3
# del c
# max = 2
with_max = DictionaryWithMax2()
with_max.put('a', 1)
with_max.put('b', 2)
with_max.put('c', 3)
print(with_max.max())  # ('c', 3)

with_max.delete('c')
print(with_max.max())  # ('b', 2)

with_max.put('a', 10)
print(with_max.max())  # ('a', 10)

with_max.put('b', 20)
print(with_max.max())  # ('b', 20)
