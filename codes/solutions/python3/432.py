from collections import defaultdict


class Node:
    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.next = None
        self.pre = None


class AllOne:

    def __init__(self):
        self.first = {}
        self.last = {}
        self.keys = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def add(self, prev, node):
        node.pre = prev
        node.next = prev.next
        node.pre.next = node.next.pre = node

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def process(self, node):
        if self.last[node.val] == node and node.pre.val != node.val:
            self.first.pop(node.val)
            self.last.pop(node.val)
        elif self.first[node.val] == node:
            self.first[node.val] = node.next
        elif self.last[node.val] == node:
            self.last[node.val] = node.pre

    def process2(self, node, prev, key, d):
        if key in self.keys:
            if node.val + d in self.last:
                self.add(self.last[node.val + d], node)
            elif node.val in self.last:
                self.add(self.last[node.val], node)
            else:
                self.add(prev, node)
        elif 1 in self.last:
            node = Node(key, 0)
            self.add(self.last[1], node)
        else:
            node = Node(key, 0)
            self.add(self.head, node)
        node.val += d
        self.last[node.val] = node
        if node.val not in self.first:
            self.first[node.val] = node
        if key not in self.keys:
            self.keys[key] = node

    def inc(self, key):
        if key in self.keys:
            node = self.keys[key]
            prev = node.pre
            self.process(node)
            self.remove(node)
            self.process2(node, prev, key, 1)
        else:
            self.process2(None, None, key, 1)

    def dec(self, key):
        if key in self.keys:
            node = self.keys[key]
            prev = node.pre
            self.process(node)
            self.remove(node)
            if node.val != 1:
                self.process2(node, prev, key, -1)
            else:
                self.keys.pop(key)

    def getMaxKey(self):
        return self.tail.pre.key if self.tail.pre != self.head else ""

    def getMinKey(self):
        return self.head.next.key if self.head.next != self.tail else ""


from sortedcontainers import SortedDict


class AllOne2:

    def __init__(self):
        self.original_mp = defaultdict(int)
        self.value_mp = SortedDict()

    def inc(self, key: str) -> None:
        prev_v = self.original_mp[key]
        self.original_mp[key] += 1
        new_v = self.original_mp[key]
        if prev_v > 0:
            self.value_mp[prev_v].remove(key)
            if not self.value_mp[prev_v]:
                del self.value_mp[prev_v]

        self.value_mp.setdefault(new_v, set()).add(key)

    def dec(self, key: str) -> None:
        prev_v = self.original_mp[key]
        self.original_mp[key] -= 1

        self.value_mp[prev_v].remove(key)
        # remove from original map if zero
        if self.original_mp[key] == 0:
            self.original_mp.pop(key)
        else:
            # add the new value back to value map
            self.value_mp.setdefault(prev_v - 1, set()).add(key)

        # clean value map if no key for this value
        if not self.value_mp[prev_v]:
            self.value_mp.pop(prev_v)

    def getMaxKey(self) -> str:
        return self.value_mp.peekitem()[0] if self.value_mp else ''

    def getMinKey(self) -> str:
        return self.value_mp.peekitem(0)[0] if self.value_mp else ''

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


import random
random.randint(0,4)