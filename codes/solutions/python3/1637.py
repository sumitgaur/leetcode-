# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def lca(p, q: Node):
    p_parents = set()
    while p:
        p_parents.add(p)
        p = p.parent
    while q:
        if q in p_parents:
            return q
        q = q.parent


def lca_2(p, q: Node):
    pointer_a, pointer_b = p, q
    while pointer_a != pointer_b:
        pointer_a = pointer_a.parent if pointer_a else 
