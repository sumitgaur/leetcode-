from collections import defaultdict
from typing import List


def reverse_in_group(s, k):
    s = "abcd"
    k = 2
    res = ""
    for i in range(0, len(s), 2 * k):
        t = s[i:i + 2 * k]
        res += t[:k][::-1] + t[k:]
    print(res)


def criticalConnections(n, connections):
    adj = defaultdict(list)
    res = set()
    for a, b in connections:
        adj[a].append(b)
        adj[b].append(a)
    for node, edges in adj.items():
        if len(edges) == 1:
            res.add(tuple(sorted([node, edges[0]])))
    return list(map(lambda x: list(x), res))


def restoreIpAddresses(s: str) -> List[str]:
    def valid(s):
        return 0 <= int(s) <= 255

    def splits(s, n):
        if n == 1:
            return [s] if valid(s) else []

        valid_parts = []
        for i in range(3):
            if valid(s[:i + 1]):
                valid_later_parts = splits(s[i + 1:], n - 1)
                valid_parts += [s[:i + 1] + "." + x for x in valid_later_parts]
        return valid_parts

    return splits(s, 4)


def reverse_vowels(s):
    i, j = 0, len(s)-1
    ls = list(s)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while i < j:
        if ls[i] not in vowels:
            i += 1
            continue
        if ls[j] not in vowels:
            j -= 1
            continue
        ls[i], ls[j] = ls[j], ls[i]
        i, j = i + 1, j - 1
    return ''.join(ls)
    # print(criticalConnections(6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]))


print(reverse_vowels("hello"))

# restoreIpAddresses("25525511135")
