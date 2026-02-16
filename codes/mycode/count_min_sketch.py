# count min sketch
import hashlib


class CMS:
    def __init__(self, k=10, w=100):
        self.k = k
        self.w = w
        self.table = [[0] * w for _ in range(k)]

    def add(self, word):
        for i in range(self.k):
            j = self._hash(i, word) % self.w
            self.table[i][j] += 1

    def _hash(self, i, word):
        return int(hashlib.sha256(f'{word}_{i}'.encode()).hexdigest(), 16)

    def count(self, word):
        return min(self.table[i][self._hash(i, word) % self.w] \
                   for i in range(self.k))


cms = CMS()
cms.add("apple")
cms.add("apple")
cms.add("orange")
cms.add("banana")
cms.add("apple")

print(cms.count("apple_1"))
