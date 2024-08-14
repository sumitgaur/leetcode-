from collections import defaultdict


def delete_tree_nodes(value, parent):
    graph = defaultdict(list)
    n = len(parent)
    for i in range(n):
        graph[parent[i]].append(i)

    def dfs(u):
        s, m = value[u], 1
        for v in graph[u]:
            i, j = dfs(v)
            s += i
            m += j

        if s == 0:
            m = 0
        return s, m

    return dfs(0)


nodes = 7
parent = [-1, 0, 0, 1, 2, 2, 2]
value = [1, -2, 4, 0, -2, -1, -2]
print(delete_tree_nodes(value, parent))
