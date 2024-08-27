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


def decompress(compressed):
    decompressed = []
    i = 0
    while i < len(compressed):
        if compressed[i] == 0xFE:
            length = compressed[i + 1]
            offset = compressed[i + 2]
            start = len(decompressed) - offset
            j = 0
            while j < len(decompressed):
                decompressed.append(decompressed[start + j])
                j += 1
            i += 3
        else:
            decompressed.append(compressed[i])
            i += 1
    return ''.join(map(chr, decompressed))


# Compressed data for "ABRA KEDABRA DABRA"
compressed_data = [ord('A'), ord('B'), ord('R'), ord('A'), ord(' '), ord('K'), ord('E'), ord('D'), 0xFE, 4, 7, 0xFE, 5,
                   5]
compressed_data = [ord('A'), 0xFE, 8, 0]
# Decompress and print the result
print(decompress(compressed_data))

if __name__ == '__main__':
    A = [0, 1, 1]
    B = [1, 2, 3]

    print(Solution(A, B))
