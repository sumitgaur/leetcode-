# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def traverse(arr):
            if arr == []: return
            node = TreeNode(arr[len(arr) // 2])
            node.left = traverse(arr[:len(arr) // 2])
            node.right = traverse(arr[len(arr) // 2 + 1:])
            return node

        array = []
        while head: array.append(head.val); head = head.next
        return traverse(array)

    def build_tree(self, arr, l, r):
        if l <= r:
            m = (l + r) // 2
            root = TreeNode(arr[m])
            root.left = self.build_tree(arr, l, m - 1)
            root.right = self.build_tree(arr, m + 1, r)
            return root
        return None


arr = [-10, -3, 0, 5, 9]

Solution().build_tree(arr, 0, 4)
