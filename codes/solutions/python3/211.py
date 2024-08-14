class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.last = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            if not curr.children[ord(char) - ord("a")]: curr.children[ord(char) - ord("a")] = TrieNode()
            curr = curr.children[ord(char) - ord("a")]
        curr.last = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        words = [self.root]
        for char in word:
            if char == ".":
                words = [child for node in words for child in node.children if node and child]
            else:
                words = [node.children[ord(char) - ord("a")] for node in words if
                         node and node.children[ord(char) - ord("a")]]
        if words and words[-1] == ".":
            return True
        else:
            return any([node.last for node in words if node.last])


class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["END"] = True

    def search(self, word: str) -> bool:
        def do(cur, w):
            if len(w) == 0:
                return "END" in cur
            if w[0] in cur:
                return do(cur[w[0]], w[1:])
            if w[0] == '.':
                return any(do(cur[c], w[1:]) for c in cur.keys() if c != "END")
            return False

        return do(self.trie, word)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
print(obj.search("bad"))
obj.addWord("dad")
obj.addWord("mad")
obj.addWord("pad")
obj.addWord("bad")
print(obj.search(".ad"))
print(obj.search("b.."))
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
