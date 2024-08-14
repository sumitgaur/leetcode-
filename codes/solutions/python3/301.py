class Solution:
    def removeInvalidParentheses(self, s):
        l = r = 0
        for c in s:
            if c.isalpha(): continue
            if c == "(":
                l += 1
            elif l:
                l -= 1
            else:
                r += 1
        q = {("", l, r, 0, 0)}
        for c in s:
            new = set()
            for st, l, r, lCur, rCur in q:
                if c == "(":
                    new.add((st + c, l, r, lCur + 1, rCur))
                    if l:
                        new.add((st, l - 1, r, lCur, rCur))
                elif c == ")":
                    if lCur:
                        new.add((st + c, l, r, lCur - 1, rCur))
                    else:
                        new.add((st + c, l, r, lCur, rCur + 1))
                    if r:
                        new.add((st, l, r - 1, lCur, rCur))
                else:
                    new.add((st + c, l, r, lCur, rCur))
            q = new
        return list({st for st, l, r, lCur, rCur in q if l == r == lCur == rCur == 0})

    def removeInvalid(self, s):sumn
        st = []
        in_ = list(s)
        for i in range(len(in_)):
            if in_[i] == '(':
                st.append(i)
            elif in_[i] == ')':
                if not st:
                    in_[i] = ""
                else:
                    st.pop()
        while st:
            in_[st.pop()] = ""
        return "".join(in_)


s = "(a)())()"
print(Solution().removeInvalid(s))
