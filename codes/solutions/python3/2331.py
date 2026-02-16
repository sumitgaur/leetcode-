# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root:
            if root.left is None and root.right is None:
                return bool(root.val)
            l = self.evaluateTree(root.left)
            r = self.evaluateTree(root.left)
            if root.val == 2:
                return l or r
            return l and r


class OperandException(Exception):
    def __init__(self):
        pass


class OperatorException(Exception):
    def __init__(self):
        pass
# Node definition
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Expression:
#            (/)
#           /   \
#        (*)     4
#       /   \
#      2     (+)
#           /   \
#          3     (/)
#               / \
#              6   2


class EvaluateExpression:
    def evaluateTree(self, root):
        if root:
            if root.left is None and root.right is None:
                if isinstance(root.val, int):
                    return root.val
                else:
                    raise OperandException(f'Invalid operand {root.val}')
            if root.val not in ['/', '*', '+', '-']:
                raise OperatorException(f'Invalid Operator {root.val}')
            try:
                l = self.evaluateTree(root.left)
                r = self.evaluateTree(root.right)
                if root.val == '/': return l/r
                if root.val == '*': return l*r
                if root.val == '+': return l+r
                if root.val == '-': return l-r
            except Exception as e:
                print(f'Exception occurred {e}')


root = Node(
    '*',
    Node(2),
    Node(
        '/',
        Node(6),
        Node(0)
    )
)

print(EvaluateExpression().evaluateTree(root))