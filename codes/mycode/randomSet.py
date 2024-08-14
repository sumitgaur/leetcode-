import random


class RandomizedSet:

    def __init__(self):
        self.table = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val not in self.table:
            self.l.append(val)
            self.table[val] = len(self.l) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.table:
            i = self.table[val]
            self.l[-1], self.l[i] = self.l[i], self.l[-1]
            self.table[self.l[i]]=i
            self.l.pop()
            self.table.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return self.l[random.randrange(len(self.l))]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

print(obj.insert(0))
print(obj.insert(1))
print(obj.remove(0))
print(obj.insert(2))
print(obj.remove(1))

print(obj.getRandom())
