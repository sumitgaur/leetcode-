from collections import OrderedDict

memo = {}


def rename_file(new_name, old_name):
    if new_name == old_name or new_name == "":
        return 1
    if old_name == "" or len(new_name) > len(old_name):
        return 0

    if (new_name, old_name) in memo:
        return memo[(new_name, old_name)]
    if new_name[0] == old_name[0]:
        memo[(new_name, old_name)] = do(new_name[1:], old_name[1:]) + do(new_name, old_name[1:])
    else:
        memo[(new_name, old_name)] = do(new_name, old_name[1:])
    return memo[(new_name, old_name)]


def replace_non_repeat(s):
    s = list(s)
    non_repeating = [s[0]]
    seen = set(s[0])
    res = [s[0]]
    for i in range(1, len(s)):
        if non_repeating:
            if non_repeating[0] != s[i]:
                res.append(non_repeating[0])
            else:
                non_repeating.pop(0)
                res.append(non_repeating[0] if non_repeating else "#")
        else:
            res.append(s[i])
        if s[i] not in seen:
            non_repeating.append(s[i])
            seen.add(s[i])
        elif s[i] in non_repeating:
            non_repeating.remove(s[i])

    return "".join(res)


def noPrefix(words):
    root = {}
    for word in words:
        cur = root
        for c in word:
            cur[c] = cur.get(c, {})
            if "END" in cur:
                print("BAD SET\n" + word)
                return
            cur = cur[c]
        cur["END"] = True
    print("GOOD SET")


noPrefix(["abcd", "bcd", "abcde", "bcde"])
