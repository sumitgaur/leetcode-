"""
Implement an in-memory cache with eviction policy
1. Support eviction policy - LRU, LFU etc.
2. Support GET/PUT -
3. optional TTL
4. thread safe
"""
from abc import abstractmethod, ABC
from collections import OrderedDict
import heapq


# strategies
class EvictionPolicy(ABC):

    @abstractmethod
    def remove_key(self):
        pass

    @abstractmethod
    def key_accessed(self, key):
        pass

    @abstractmethod
    def store(self, key, value):
        pass

    @abstractmethod
    def retrieve(self, key):
        pass


# concrete strategies
class LRUEviction(EvictionPolicy):
    def __init__(self):
        self.data_store = OrderedDict()

    def remove_key(self):
        self.data_store.popitem(last=False)

    def key_accessed(self, key):
        self.data_store.move_to_end(key)

    def store(self, key, value):
        self.data_store[key] = value

    def retrieve(self, key):
        return self.data_store.get(key, None)


class HeapNode:
    def __init__(self, frequency, key, value):
        self.frequency = frequency
        self.key = key
        self.value = value

    def __le__(self, other):
        return self.frequency < other.frequency


class LFUEviction(EvictionPolicy):

    def __init__(self):
        self.pq = []  # [(frequency,key,value)] min heap
        self.mp = {}  # {key:heap_node}

    def remove_key(self):
        heap_node = heapq.heappop(self.pq)
        self.mp.pop(heap_node.key)

    def key_accessed(self, key):
        heap_node = self.mp[key]
        heap_node.frequency += 1
        heapq.heapify(self.pq)

    def store(self, key, value):
        heap_node = HeapNode(0, key, value)
        self.mp[key] = heap_node
        heapq.heappush(self.pq, heap_node)

    def retrieve(self, key):
        heap_node = self.mp[key]
        self.key_accessed(key)
        return heap_node.value


class Cache:
    def __init__(self, capacity, eviction_policy: EvictionPolicy):
        self.capacity = capacity
        self.cache_size = 0
        # self.ttl = ttl
        self.eviction = eviction_policy

    def get(self, key):
        self.eviction.key_accessed(key)
        return self.eviction.retrieve(key)

    def put(self, key, value):
        if self.cache_size >= self.capacity:
            self.eviction.remove_key()
        self.eviction.store(key, value)


eviction_policy = LRUEviction()
cache = Cache(5, eviction_policy)
cache.put('a', 'amit')
cache.put('s', 'sumit')
print(cache.get('s'))

cache.put('s2', 'sumit2')
cache.put('s3', 'sumit3')
print(cache.get('s3'))
cache.put('s4', 'sumit4')
cache.put('s5', 'sumit5')
print(cache.get('s2'))
