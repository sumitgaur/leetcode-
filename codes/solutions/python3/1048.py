import collections


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def dfs(w1, size):
            return max([dfs(w2, size + 1) for w2 in graph[w1]], default=size)

        graph = collections.defaultdict(list)
        for w in words:
            graph[len(w)].append(w)
        for w1 in words:
            for w2 in graph[len(w1) + 1]:
                for i in range(len(w2)):
                    if w2[:i] + w2[i + 1:] == w1:
                        graph[w1].append(w2)
        return max(dfs(w, 1) for w in words)

    def longestStrChain1(self, words):

        graph = collections.defaultdict(list)
        for w in words:
            graph[len(w)].append(w)

        levels = sorted(graph.keys())
        l = 0
        q = collections.deque(graph[levels[l]])
        longestchain = 1
        while q:
            qsize = len(q)
            next_level = set()
            while qsize:
                w1 = q.pop()
                for words in graph[l + 1]:
                    for w2 in words:
                        for i in range(l + 1):
                            if w2[:i] + w2[i + 1:] == w1:
                                next_level.add(w2)
                                break

                qsize -= 1
