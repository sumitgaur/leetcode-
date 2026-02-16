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
            i += 1
        return "".join(res[::-1])

    def addBinary3(self, a: str, b: str) -> str:
        def _sum(a, b, carry=0):
            if a == '' and b == '':
                return str(carry) if carry else ''
            if a == '':
                return _sum(str(carry), b, 0)
            if b == '':
                return _sum(a, str(carry), 0)
            else:
                s = int(a[-1]) + int(b[-1]) + carry
                return _sum(a[:-1], b[:-1], s // 2) + str(s % 2)

        return _sum(a, b)


s = Solution()
print(s.addBinary3("1010", "1011"))
