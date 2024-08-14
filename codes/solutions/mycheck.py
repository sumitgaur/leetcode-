import math
from collections import defaultdict


def Solution(A, B):
    connections = defaultdict(list)
    for a, b in zip(A, B):
        connections[a].append(b)
        connections[b].append(a)

    visited = set()

    def cost(x):
        if all(y in visited for y in connections[x]):
            return 1, 0
        x_cost, x_people = 0, 1
        for y in connections[x]:
            if y not in visited:
                visited.add(y)
                people_count, y_cost = cost(y)
                x_cost += y_cost + math.ceil(people_count / 5)
                x_people += people_count
        return x_people, x_cost

    visited.add(0)
    _, total = cost(0)
    return total


if __name__ == '__main__':
    A = [0, 1, 1]
    B = [1, 2, 3]

    print(Solution(A, B))
