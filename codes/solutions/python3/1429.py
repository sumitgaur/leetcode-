from collections import OrderedDict, Counter


class FirstUnique:
    def __init__(self, arr):
        self.queue = Counter()
        self.ordered_unique = OrderedDict()
        for x in arr:
            self.add(x)

    def add(self, x):
        if x in self.queue:
            self.ordered_unique.pop(x)
        else:
            self.ordered_unique[x] = True
        self.queue[x] += 1

    def showFirstUnique(self):
        print(next(iter(self.ordered_unique))) if self.ordered_unique else print(-1)


fq = FirstUnique([2, 3, 5])
fq.showFirstUnique()
fq.add(5)
fq.showFirstUnique()
fq.add(2)
fq.showFirstUnique()
fq.add(3)
fq.showFirstUnique()
