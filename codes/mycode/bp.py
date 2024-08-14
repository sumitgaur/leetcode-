"""

Code a data structure which allows us to store and retrieve items by key up to a fixed capacity
When we add items over capacity we free up space by removing an item first:

1) remove any expired item first
2) If there are no expired items, find the items with the lowest priority number, and remove the one which has been used least recently of them

S = new Store(5)
// S.Set(key="A", value=5, priority=5, expiration=10001)
//S.Set(key="B", value=4, priority=1, expiration=40006)
S.Set(key="C", value=3, priority=5, expiration=10001)
// S.Set(key="D", value=2, priority=9, expiration= 500)
//S.Set(key="E", value=1, priority=5, expiration=10004)
S.Get("C")

// Current Time = 900 system.get_current_time()
S.Set(key="F", value=10, priority=5, expiration= 5001)
S.Set(key="G", value=9, priority=5, expiration= 5004)
S.Set(key="H", value=-1, priority=5, expiration= 5009)
S.Set(key="I", value=1, priority=5, expiration= 5011)
S.Set(key="C", value=1, priority=5, expiration= 5021) // update key with new value etc :

S.Get("D") // return null/notpresent


"""

# LinkedHashMap suggested for LRU
# k <v,index_of_expiration_heap,index_of_priority_heap>
# Remove/reinsert for updating elements
# currenttime > expiration , evict the element,

# 2 min heaps with one keeping expiration nodes and other will keep priority based nodes  O(lgn)
# O(1) to get the near expiration
# worst number of element O(C) in all of these ds
from collections import OrderedDict
from heapq import heappush, heappop
import time


class Cache:
    def __init__(self, capacity) -> None:
        self.n = capacity
        self.cache_map = OrderedDict()  # LRU
        self.expiration_heap = []
        self.priorirty_heap = []

    # time complexity: O(1)
    def get(self, k):
        if k in self.cache_map:
            v, i, j = self.cache_map.pop(k)  # O(1)
            self.cache_map[k] = (v, i, j)  # O(1)
            return v
        else:
            return None

            # time complexity: O(lgn)

    def put(self, k, v):
        if k in self.cache_map:
            v, exp_ind, pri_ind = self.cache_map.pop(k)
            # remove from heaps
            self.remove_from_heap(self.expiration_heap, exp_ind)
            self.remove_from_heap(self.priorirty_heap, pri_ind)
            # add to heaps
            exp_ind = self.add_to_heap(self.expiration_heap, k)
            pri_ind = self.add_to_heap(self.priorirty_heap, k)
            self.cache_map[k] = (v, exp_ind, pri_ind)
        else:
            if len(self.cache_map) >= self.n:
                # eviction
                if self.expiration_heap[0] < time.time():
                    k = heappop(self.expiration_heap)
                    _, _, ind_pri = self.cache_map.pop(k)
                    self.remove_from_heap(self.priorirty_heap, k)
                else:
                    same_priority_keys = [heappop(self.priorirty_heap)]

                    # O(log n)
                    # maintain separate data structure which can kee frequency map of priorities
                    # priority: element
                    # priority -> List of Elements with Priority
                    # data structure? Map

                    while same_priority_keys[0] == self.priorirty_heap[
                        0]:  # nlgn/n worst case if all are same priority
                        same_priority_keys.append(heappop(self.priorirty_heap))

                    # find the LRU < O(n)?
                    # can we get this lower?

                    # find the lowest priority - priority heap    // you can store same priority keys in the same node of the heap and keep in LRU order 
                    # collection of items with the lowest priority  # O(n) <- can we get to O(log n)?? binary search to find start and end index
                    # the item has been LRU
                    # Keep it ordered by LRU
                    # -> collection -> sorted list #
                    # at the time you get the lowest priority - decrease variable ->

                    # LRU aspect originally: OrderedDictionary : this is implemented DLL and a Dictionary
                    # dictionary holds nodes to DLL

                    # could use BST? per priority -> BST ->

                    for k in same_priority_keys:  # O(n)
                # self.cache_map get keys

    def add_to_heap(self, h, element):
        """
        insert element into the heap h and return the node refrence  O(lg(n))
        """
        pass

    def remove_from_heap(self, h, element):
        """
        remove the element from the heap h   O(lg(n))
        """
        pass



