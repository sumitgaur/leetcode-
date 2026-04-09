# Given trips (start, end, passengers), check if carpool capacity exceeds limit
from collections import deque, defaultdict


def min_drivers_required(trips):
    sweep = []
    for s, e, p in trips:
        sweep.append([s, p])
        sweep.append([e, -p])
    sweep.sort(key=lambda x: x[0])
    cur_max = 0
    gl_max = 0
    for t, p in sweep:
        cur_max += p
        gl_max = max(gl_max, cur_max)
    return gl_max


# Find shortest path where you can skip at most K blocked edges
def shortest_path_skip_k_blocked_edges(graph, start, end, k):
    bfs = deque([start, 0, 0])
    visited = set([(start, k)])
    while bfs:
        node, skips, dist = bfs.popleft()
        if node == end: return dist
        for nei, blocked in graph[node]:
            if not blocked and (nei, skips) not in visited:
                visited.add((nei, skips))
                bfs.append((nei, skips, dist + 1))

            if blocked and skips > 0 and (nei, skips - 1) not in visited:
                visited.add((nei, skips - 1))
                bfs.append((nei, skips - 1, dist + 1))

    return -1


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, node):
        while node != self.parent[node]:
            node = self.parent[node]
        return self.parent[node]

    def union(self, node1, node2):
        p1 = self.find(node1)
        p2 = self.find(node2)
        if p1 != p2:
            self.parent[p1] = p2


# You are given bus routes. Each route is a list of stops.
# Find minimum buses needed from source → target.

def min_buses_needed(routes, source, target):
    stop_to_buses = defaultdict(list)
    for bus_ind, route in enumerate(routes):
        for stop in route:
            stop_to_buses[stop].append(bus_ind)
    q = deque([source, 0])
    visited_bus = set()
    visited_stops = set()
    while q:
        stop, buses_taken = q.popleft()
        for bus in stop_to_buses[stop]:
            if bus not in visited_bus:
                visited_bus.add(bus)
                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses_taken
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        q.append([next_stop, buses_taken + 1])
    return -1


# routes = [[1,2,7],[3,6,7]]
# source = 1
# target = 6
# 1->1
# 2->1
# 7->1,2
# 3->2
# 6->2

def alien_dict(words):
    graph = defaultdict(set)
    indegree = defaultdict(int)
    for w1, w2 in zip(words, words[1:]):
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph:
                    graph[c1].add(c2)
                    indegree[c2] += 1
            break

    q = deque([c for c in indegree if indegree[c] == 0])
    res = []
    while q:
        c = q.popleft()
        res.append(c)
        for c2 in graph[c]:
            indegree[c2] = -1
            if indegree[c2] == 0:
                q.append(c2)

    return "".join(res)
