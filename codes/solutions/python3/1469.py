class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


ans = []


def get_lonely_nodes(root):
    if root is None or (root.left is None and root.right is None):
        return []
    if root.left is None:
        return [root.right.val]
    if root.right is None:
        return [root.left.val]
    return get_lonely_nodes(root.left) + get_lonely_nodes(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

print(get_lonely_nodes(root))
