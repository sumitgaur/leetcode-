
def StringChallenge(strParam):
    def check(s):
        digits = 0
        for a, b in zip(s, s[1:]):
            if a.isdigit() and b.isdigit():
                return False
            if a.isdigit():
                digits += 1
            if digits > 3:
                return False
        return True

    return all(map(check, strParam.split(" ")))


import collections


def NameCollection(strArr):
    def cmp_(n1, n2):
        f1, l1 = n1.rsplit(" ", 1)
        f2, l2 = n2.rsplit(" ", 1)
        l1_most_ = collections.Counter(l1).most_common(1)[0][1]
        l2_most_ = collections.Counter(l2).most_common(1)[0][1]
        if l1_most_ != l2_most_:
            return 1 if l1_most_ > l2_most_ else -1

        if l1 != l2:
            return 1 if l1 > l2 else -1

        return 1 if f1 > f2 else -1

    from functools import cmp_to_key
    return sorted(strArr, key=cmp_to_key(cmp_))


from collections import Counter


def ArrayChallenge(arr):
    pairs = Counter()
    res = []

    for i in range(0, len(arr) - 1, 2):
        pairs[(arr[i + 1], arr[i])] += 1
    for i in range(0, len(arr), 2):
        if (arr[i], arr[i + 1]) not in pairs:
            res += [arr[i], arr[i + 1]]
        if (arr[i] == arr[i + 1]) and pairs[(arr[i], arr[i + 1])] < 2:
            res += [arr[i], arr[i + 1]]

    return ",".join(map(str, res)) if res else "yes"


# keep this function call here
print(NameCollection(["B ABB Irmottti", "ABB ASD juju Irmottti"]))

# print(StringChallenge("2a3b5 w1o2rl3d g1gg92"))
