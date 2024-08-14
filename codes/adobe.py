# Implement a LRU cache with a fixed capacity
# +get(key)
# +put(key)
#
from collections import OrderedDict


class Node:
    """
    DLL node
    """

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None


class LRU:
    def __init__(self, capacity):
        if capacity < 1:
            raise Exception("Capactity should be greater than 0")
        self.capacity = capacity
        self.size = 0
        self.node_map = {}
        self.head = None  # most recent used keys
        self.tail = None  # least recent used keys

    def _use_node(self, node):
        """
        put a node at the head
        :param node:
        :return:
        """
        if node is self.head: return
        if node.next: node.next.prev = node.prev
        if node.prev: node.prev.next = node.next
        if node is self.tail:
            self.tail = self.tail.prev
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node

    def get(self, key):
        """
        return the value of the key if ppresent otherwise Key error
        :param key:
        :return:
        """
        if key in self.node_map:
            self._use_node(self.node_map[key])
            return self.node_map[key].val
        raise KeyError("Key doesn't exist in the cache")

    def put(self, k, v):
        """
        put the k and valu, if already present update the value
        :param k:
        :param v:
        :return:
        """
        if k in self.node_map:
            self._use_node(self.node_map[k])
            self.node_map[k].val = v
        else:
            node = Node(k, v)
            self.node_map[k] = node
            if self.size == 0:
                self.head = node
                self.tail = node
            if self.size < self.capacity:
                self.size += 1
            elif self.size == self.capacity:  # eviction
                k = self.tail.key
                if self.size == 1:
                    self.head = node
                    self.tail = node
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
                del self.node_map[k]
        self._use_node(node)


if __name__ == '__main__':
    lru = LRU(3)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)
    print(lru.get(2))
    print(lru.get(1))
    lru.put(4, 4)
    print(lru.get(4))

# 1<->2<->4   values
# 0   1   2   3
# mp:{
#     1->0
#     2->1
#     3->2
#        // pput(3,4)
# }
#
# put(1,0)  // a->
# put(2,1)  // a->b
# put(3,2)  // a->b->c
# put(3,'d')  //
#
#
# mp.get(k) {
#     node=_intermap.get(x) ; node.val
# }
# mp.get()
