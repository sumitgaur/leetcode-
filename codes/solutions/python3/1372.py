# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def do(root, dir):
            if root:
                if dir == -1:
                    return max(1 + do(root.right, 1), do(root.left, -1))
                else:
                    return max(1 + do(root.left, -1), do(root.left, 1))
            return 0

        l = 1 + do(root.left, -1) if root.left else 0
        r = 1 + do(root.right, 1) if root.right else 0
        return max(l, r)
