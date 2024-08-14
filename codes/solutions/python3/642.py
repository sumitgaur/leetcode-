# class AutocompleteSystem:
#
#     def __init__(self, sentences: List[str], times: List[int]):
#         self.cur = self.root = {}
#         self.rank = collections.defaultdict(int)
#         for i, s in enumerate(sentences):
#             self.s = s
#             self.rank[s] = times[i] - 1
#             self.input('#')
#
#     def move(self, c):
#         if c not in self.cur:
#             self.cur[c] = {}
#         self.cur = self.cur[c]
#         if 'sentences' not in self.cur:
#             self.cur['sentences'] = []
#
#     def addSentence(self):
#         self.cur = self.root
#         for c in self.s:
#             self.move(c)
#             self.search()
#             heapq.heappush(self.cur['sentences'], [-self.rank[self.s], self.s])
#
#     def search(self):
#         q, used, i = [], set(), 0
#         while i < 3 and self.cur['sentences']:
#             r, s = heapq.heappop(self.cur['sentences'])
#             if s not in used:
#                 used.add(s)
#                 q.append([r, s])
#                 i += 1
#         for r, s in q:
#             heapq.heappush(self.cur['sentences'], [r, s])
#         return [s for r, s in q]
#
#     def input(self, c: str) -> List[str]:
#         if c == '#':
#             self.rank[self.s] += 1
#             self.addSentence()
#             self.s = ''
#             self.cur = self.root
#             return []
#         else:
#             self.s += c
#             self.move(c)
#             return self.search()


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

from collections import defaultdict, Counter
import heapq

from django.utils.lorem_ipsum import sentence


class AutoComplete:
    def __init__(self, sentences, times):
        self.sentences = sentences
        self.times = times
        self.prefix_sentences_map = defaultdict(list)  # dict to heap
        for s, t in zip(sentences, times):
            self.prefix_populate(s, t)

    def prefix_populate(self, sentence, times):
        heapq.heappush(self.prefix_sentences_map[" "], [-times, sentence])
        for i in range(len(sentence)):
            heapq.heappush(self.prefix_sentences_map[sentence[:i + 1]], [-times, sentence])

    def most_common(self, prefix, k):
        sentences_heap = self.prefix_sentences_map[prefix]
        copy_heap = sentences_heap[:]
        res = []
        while copy_heap and k:
            x = [heapq.heappop(copy_heap)]
            while copy_heap and copy_heap[0][0] == x[-1][0]:
                x.append(heapq.heappop(copy_heap))
            res.append(sorted(x, key=lambda y: y[1])[0][1])
            k -= 1
        return res


if __name__ == '__main__':
    auto_complete = AutoComplete(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
    print(auto_complete.most_common("i", 3))
