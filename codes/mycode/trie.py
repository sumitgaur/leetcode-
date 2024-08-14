# class Trie:
#     def __init__(self):
#         self.levels = []
#         self.pairs = 0
#
#     def insert(self, s):
#         new_branch = 0
#         paired = 0
#         for l, c in enumerate(s):
#             if l + 1 > len(self.levels):
#                 self.levels.append({c})
#             elif c not in self.levels[l]:
#                 paired += len(self.levels[l])
#                 self.levels[l].add(c)
#                 new_branch += 1
#         self.pairs += paired if new_branch == 1 else 0
#
#     def show_levels(self):
#         print(self.levels)

class Trie:
    def __init__(self):
        self.levels = []

    def insert(self, string):
        new_branches = 0
        for level in range(len(string)):
            c = string[level]
            if (level + 1) > len(self.levels):
                self.levels.append({c})
                new_branches += 1
            else:
                level_nodes = self.levels[level]
                if c not in level_nodes: # could be implemented in O(1)
                    level_nodes.add(c)
                    new_branches += 1
        return new_branches


def fun(strings):
    trie = Trie()
    for string in strings:
        new_branches = trie.insert(string)
        if new_branches == 1:
            return True
    return False
# t = Trie()
words = ["abc", "cab", "cbd"]
# for s in words:
#     t.insert(s)
print(fun(words))
