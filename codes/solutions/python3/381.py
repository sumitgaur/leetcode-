# class RandomizedCollection:
#
#     def __init__(self):
#         self.arr, self.pos = [], collections.defaultdict(set)
#     def insert(self, val):
#         out = val not in self.pos
#         self.arr.append(val)
#         self.pos[val].add(len(self.arr) - 1)
#         return out
#
#     def remove(self, val):
#         if val in self.pos:
#             if self.arr[-1] != val:
#                 x, y = self.pos[val].pop(), self.arr[-1]
#                 self.pos[y].discard(len(self.arr) - 1)
#                 self.pos[y].add(x)
#                 self.arr[x] = y
#             else:
#                 self.pos[val].discard(len(self.arr) - 1)
#             self.arr.pop()
#             if not self.pos[val]:
#                 self.pos.pop(val)
#             return True
#         return False
#
#     def getRandom(self):
#         return random.choice(self.arr)


from collections import defaultdict
from random import randrange


class RandomizedCollection:

    def __init__(self):
        self.table = defaultdict(set)
        self.list_ = []

    def insert(self, val: int) -> bool:
        res = val not in self.table
        self.list_.append(val)
        self.table[val].add(len(self.list_) - 1)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.table
        if self.list_[-1] == val:
            self.table[val].remove(len(self.list_) - 1)
            self.list_.pop()
        else:
            pop_idx = next(iter(self.table[val]))  # popping index
            last_val = self.list_[-1]  # last elt
            self.list_[-1], self.list_[pop_idx] = self.list_[pop_idx], self.list_[-1]  # swap
            # update indexes of existing elt
            self.table[last_val].remove(len(self.list_) - 1)
            self.table[last_val].add(pop_idx)

            # pop from table and list
            self.table[val].remove(pop_idx)
            self.list_.pop()
        if not self.table[val]:
            self.table.pop(val)
        return res

    def getRandom(self) -> int:
        return self.list_[randrange(len(self.list_))]

# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_1 = obj.insert(1)
param_3 = obj.getRandom()