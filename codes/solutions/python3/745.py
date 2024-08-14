import collections


class WordFilter:
    def __init__(self, words):
        self.p, self.s, self.ind = collections.defaultdict(set), collections.defaultdict(set), {}
        for i, w in enumerate(words): 
            self.ind[w] = i
            self.p[""].add(w)
            self.s[""].add(w)
            for i in range(1, len(w) + 1): 
                self.p[w[:i]].add(w)
                self.s[w[-i:]].add(w)
    def f(self, prefix, suffix): return max((self.ind[c] for c in self.p[prefix] & self.s[suffix]), default = -1)


class WordFilter2:
    def __init__(self,words):
        self.p = collections.defaultdict(set)
        self.s = collections.defaultdict(set)
        self.ind={}
        for i,w in enumerate(words):
            self.ind[w]=i
            self.p[""].add(w)
            self.s[""].add(w)
            for i in range(len(w)):
                self.p[w[:i + 1]].add(w)
                self.s[w[-i - 1:]].add(w)

    def f(self, pref: str, suff: str) -> int:
        return max((self.ind[x] for x in self.p[pref] & self.s[suff]), default=-1)
wf=WordFilter2(["apple","ape","apply","broker","broke","banana"])
print(wf.f("a","y"))
