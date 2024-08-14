class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary_2(self, a: str, b: str) -> str:
        c, i = 0, 0
        res = ""
        a, b = a[::-1], b[::-1]
        if len(a) < len(b):
            a, b = b, a
        while i < len(a) or c:
            c, x = divmod((i < len(a) and int(a[i]) or 0) + (i < len(b) and int(b[i]) or 0) + c, 2)
            res += str(x)
            i+=1
        return "".join(res[::-1])


s = Solution()
print(s.addBinary_2("1010", "1011"))
