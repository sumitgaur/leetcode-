class Node:
    def __init__(self, v):
        self.value = v
        self.left = self.right = None


def buildTree(s):
    st, i = [], 0
    while i < len(s):
        if not s[i].isdigit():
            n = Node(s[i])
            n.right = st.pop()
            n.left = st.pop()
            st.append(n)
        else:
            st.append(Node(s[i]))
        i += 1
    return st[-1]


def evaluateTree(root):
    if root.value.isdigit():
        return float(root.value)
    l = evaluateTree(root.left)
    r = evaluateTree(root.right)
    if root.value == "*":
        return l * r
    if root.value == "+":
        return l + r
    if root.value == "-":
        return l - r
    if root.value == "/":
        return l / r


s = ["4", "5", "2", "7", "+", "-", "*"]
root = buildTree(s)
print(evaluateTree(root))
