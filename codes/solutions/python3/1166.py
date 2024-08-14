import sys
from collections import defaultdict

# import numpy as np
# import pandas as pd
# from sklearn import ...

graph = defaultdict(str)


def doLinkedListsIntersect(node):
    visited_nodes = [{x} for x in (nodes)]
    if len(nodes) != len(set(nodes)):
        return True
    while not all(v is None for v in nodes):
        for i, u in enumerate(nodes):
            if u is None:
                continue
            v = graph.get(u, None)
            nodes[i] = v
            if v in visited_nodes[i]:
                raise Exception("Cycle has been detected")
            if v != None and any(v in seen for seen in visited_nodes):
                return True
            visited_nodes[i].add(v)
    return False


for line in sys.stdin:
    line=line.strip()
    if "->" in line:
        a, b = line.split("->")
        graph[a] = b
    else:
        nodes = line.split(",")
        print(doLinkedListsIntersect(nodes))