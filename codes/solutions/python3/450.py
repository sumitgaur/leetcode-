class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # Case 1: no child or one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Case 3: two children
            parent = root
            successor = root.right

            # find inorder successor (leftmost in right subtree)
            while successor.left:
                parent = successor
                successor = successor.left

            # copy value
            root.val = successor.val

            # remove successor node
            if parent == root:
                # successor is immediate right child
                parent.right = successor.right
            else:
                parent.left = successor.right

        return root
