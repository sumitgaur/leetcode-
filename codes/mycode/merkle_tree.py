class MerkleTree:
    def __init__(self):
        pass

    def reconcile(self, S1, S2):
        if S1.left == None and S2.right == None: return S1
        if S1.val == S2.val:
            return True

        return self.reconcile(S1.left, S2.left) and self.reconcile(S1.right, S1.right)




