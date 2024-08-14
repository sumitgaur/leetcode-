class Solution:
    def removeComments(self, source):
        res, block, cont, blockStart = [], False, False, -1
        for line in source:
            if not cont: cache = ""
            for i, c in enumerate(line):
                if not block: cache += c
                if cache[-2:] == "//":
                    cache = cache[:-2]
                    break
                elif cache[-2:] == "/*": blockStart, cache, block = i, cache[:-2], True
                elif line[i - 1:i + 1] == "*/" and blockStart < i - 1: block = False
            if not block:
                if cache: res += cache,
                cont = False
            else: cont, blockStart = True, -1
        return res

    def removeComments2(self,source):
        source="\n".join(source)
        res=""
        i=0
        while i<len(source):
            if source[i:i+2]=="//":
                while source[i]!="\n":
                    i+=1
            elif source[i:i+2]=="/*":
                while source[i:i+2]!="*/":
                    i+=1
                i+=2
            else:
                res+=source[i]
                i+=1
        return [l for l in res.split("\n") if l!=""]


source=["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test",
 "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
Solution().removeComments2(source)