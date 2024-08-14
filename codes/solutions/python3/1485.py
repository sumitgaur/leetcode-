# 1485 - Clone Binary Tree With Random Pointer
class Node:
    def __init__(self, v):
        self.val = v
        self.left = self.right = self.random = None


def clone_tree(root):
    original_clone = {}
    clone_original = {}

    def do(root):
        if root:
            n = Node(root.val)
            original_clone[root] = n
            clone_original[n] = root
            n.left = do(root.left)
            n.right = do(root.right)
            return n

    def populate_random(root):
        if root:
            o = clone_original[root]
            root.random = original_clone.get(o.random, None)

    n = do(root)
    populate_random(n)
    return n


def copyRandomBinaryTree(root: 'Optional[Node]') -> 'Optional[NodeCopy]':
    def dfs(root):
        if root is None:
            return None
        if root in mp:
            return mp[root]
        copy = Node(root.val)
        mp[root] = copy
        copy.left = dfs(root.left)
        copy.right = dfs(root.right)
        copy.random = dfs(root.random)
        return copy

    mp = {}
    return dfs(root)
