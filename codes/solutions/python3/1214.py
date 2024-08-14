# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from functools import lru_cache


class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def dfs(node):
            return dfs(node.left) | dfs(node.right) | {node.val} if node else set()

        q1 = dfs(root1)
        return any(target - a in q1 for a in dfs(root2))

    def twoSumBsts(self, root1, root2, target):
        def dfs(root, t1):
            if root:
                t1.add(root.val)
                dfs(root.left, t1)
                dfs(root.right, t1)

        t1, t2 = set(), set()
        dfs(root1, t1)
        dfs(root1, t2)
        return any(target - a in t1 for a in t2)


r1 = TreeNode(2)
r1.left = TreeNode(1)
r1.right = TreeNode(4)

r2 = TreeNode(1)
r2.left = TreeNode(0)
r2.right = TreeNode(3)

print(Solution().twoSumBsts(r1, r2, 5))
