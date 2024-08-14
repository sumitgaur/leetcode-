from collections import defaultdict


class FrequencyTracker:

    def __init__(self):
        self.m1 = {}
        self.m2 = {}

    def add(self, number: int) -> None:
        if number in self.m1:
            f = self.m1[number]
            self.m1[number] += 1
            if f in self.m2:
                self.m2[f] -= 1
            self.m2[f + 1] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.m1:
            f = self.m1[number]
            self.m1[number] -= 1
            if f in self.m2:
                self.m2[f] -= 1
            self.m2[f - 1] += 1

    def hasFrequency(self, f: int) -> bool:
        return f in self.m2

# Your FrequencyTracker object will be instantiated and called as such:
obj = FrequencyTracker()
obj.add(3)
obj.deleteOne(3)
param_3 = obj.hasFrequency(2)
print(param_3)
