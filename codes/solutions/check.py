def caesarCipher(s, k):
    def get_shifted_char(c, k):
        base_char = 'a' if c.islower() else 'A'
        i = ord(c) - ord(base_char)
        return chr(ord(base_char) + (i + k) % 26) if base_char <= c < chr(ord(base_char) + 26) else c

    res = ""
    for c in s:
        res += get_shifted_char(c, k)

    return res


# caesarCipher("DNFjxo?b5h*5<LWbgs6?V5{3M].1hG)pv1VWq4(!][DZ3G)riSJ.CmUj9]7Gzl?VyeJ2dIPEW4GYW*scT8(vhu9wCr]q!7eyaoy.", 45)

def palindromeIndex(s):
    def check_pal(s, i, j):
        while i < j and s[i] == s[j]:
            i, j = i + 1, j - 1
        return i >= j , i, j

    i, j = 0, len(s) - 1
    b, i, j = check_pal(s, i, j)
    if b: return -1
    b, _, _ = check_pal(s, i + 1, j)
    if b: return i
    b, _, _ = check_pal(s, i, j - 1)
    if b: return j


print(palindromeIndex('abba'))

