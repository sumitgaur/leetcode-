# 1634 - Add Two Polynomials Represented as Linked Lists
class Node:
    def __init__(self, c, p):
        self.coefficient = c
        self.power = p
        self.next = None


def addPolynomial(p1, p2):
    if p1 == None or p2 == None:
        rem = p1 or p2
        ref = n = Node(None, None)
        while rem:
            n.next = Node(rem.coefficient, rem.power)
            n, rem = n.next, rem.next
        return ref.next

    if p1.power == p2.power:
        n = Node(p1.coefficient + p2.coefficient, p1.power)
        n.next = addPolynomial(p1.next, p2.next)
    elif p1.power > p2.power:
        n = Node(p1.coefficient, p1.power)
        n.next = addPolynomial(p1.next, p2)
    else:
        n = Node(p2.coefficient, p2.power)
        n.next = addPolynomial(p1, p2.next)
    return n if n.coefficient != 0 else n.next


def print_list(r):
    while r:
        print((r.coefficient, r.power), end='')
        r = r.next
    print()


poly1 = [[1, 1]]
poly2 = [[1, 0]]
r1 = cur1 = Node(None, None)
r2 = cur2 = Node(None, None)
for c, p in poly1:
    cur1.next = Node(c, p)
    cur1 = cur1.next
for c, p in poly2:
    cur2.next = Node(c, p)
    cur2 = cur2.next
print_list(r1.next)

print_list(r2.next)
res = addPolynomial(r1.next, r2.next)
print_list(res)
