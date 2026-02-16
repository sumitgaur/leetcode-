class Trie:
    def __init__(self):
        self.root = {}

    def trie_insert(self, s):
        cur = self.root
        for c in s:
            cur = cur.setdefault(c, {})
        cur['count'] = cur.get('count', 0) + 1

    def countWordsEqualTo(self, word):
        cur = self.root
        for c in word:
            cur = cur.get(c, {})
        return cur.get('count', 0)

    def countWordsStartingWith(self, prefix):
        cur = self.root
        for c in prefix:
            cur = cur.get(c, {})
        return len(cur.keys())

    def erase(self, word):
        def dfs(node, i):
            if i == len(word):
                if 'count' not in node:
                    return False
                node['count'] -= 1
                if node['count'] == 0:
                    node.pop('count')
                # return whether this node can be deleted
                return len(node) == 0

            c = word[i]
            if c not in node:
                return False

            should_delete_child = dfs(node[c], i + 1)

            if should_delete_child:
                node.pop(c)

            # delete current node only if empty AND no word ends here
            return len(node) == 0 and 'count' not in node

        dfs(self.root, 0)


import json

t = Trie()
for w in ["abc", "cab", "cbd", "cade", "ca"]:
    t.trie_insert(w)

print(json.dumps(t.root, indent=3))

print(t.countWordsEqualTo("abc"))
print(t.countWordsStartingWith('cab'))
print(t.countWordsStartingWith('a'))
t.erase('cab')
print(json.dumps(t.root, indent=3))
print(t.countWordsStartingWith('abc'))
