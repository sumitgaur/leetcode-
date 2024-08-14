class Solution:
    def backspaceCompare(self, S, T):
        def construct(s):
            new_s = []
            for c in s:
                if c == "#" and len(new_s) > 0:
                    new_s.pop()
                elif c != "#":
                    new_s.append(c)
            return new_s
        s, t = construct(S), construct(T)
        return s == t
    def removeStars(self,s):
        stars=0
        res=""
        for x in s[::-1]:
            if x == "*":
                stars+=1
            elif stars:
                stars-=1
            else:
                res+=x
        return res[::-1]

print(Solution().removeStars("leet**cod*e"))




