# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, arr):
            if not node.right and not node.left:
                #print(arr)
                self.res += ['->'.join(str(num) for num in arr)]
            if node.left:
                dfs(node.left, arr + [node.left.val])
            if node.right:
                dfs(node.right, arr + [node.right.val])
        self.res = []
        if not root: return []
        dfs(root, [root.val])
        return self.res

    def binaryTreePaths2(self, root: TreeNode) -> List[str]:
        self.res=[]

        def do(root, path=[]):
            if root:
                path.append(root.val)
                if root.left==None and root.right==None:
                    self.res.append('->'.join(map(str, path)))
                else:
                    do(root.left, path)
                    do(root.right, path)
                path.pop()
        return self.res

r=TreeNode(1)
r.left=TreeNode(2)
r.right=TreeNode(3)
r.left.right=TreeNode(5)
Solution().binaryTreePaths2(r)
