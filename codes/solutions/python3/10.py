import re


class Solution:
    def isMatch(self, s, p):
        return bool(re.match(r"%s" % p, s)) and re.match(r"%s" % p, s).group(0) == s

    def isMatch2(self, s, p):
        def nfa(p):
            N = sum(1 for c in p if c.isalpha() or c == ".")
            Q = [{}]
            i = j = 0
            while j < len(p):
                if j + 1 < len(p) and p[j + 1] == "*":
                    Q[i][p[j]] = i
                    j = j + 2
                else:
                # if p[j] not in Q[i]:
                    Q[i][p[j]] = i + 1
                    i += 1
                    Q.append({})
                    j += 1
            return Q, i

        tran_func, F = nfa(p)
        i = 0
        for c in s:
            if c in tran_func[i]:
                i = tran_func[i][c]
            elif "." in tran_func[i]:
                i = tran_func[i]["."]
            else:
                return False
        return i == F




print(Solution().isMatch2("aaba","ab*a*c*a"))