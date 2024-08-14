from collections import defaultdict
from typing import List


class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        char1, char2, diff1, diff2, res = False, False, 0, 0, [None] * len(S)
        for i in range(len(S)):
            if char1: res[i], diff1 = min(res[i], diff1 + 1) if res[i] else diff1 + 1, diff1 + 1
            if S[i] == C: diff1, res[i], char1 = 0, 0, True
            if char2: res[len(S) - 1 - i], diff2 = min(res[len(S) - 1 - i], diff2 + 1) if res[
                len(S) - 1 - i] else diff2 + 1, diff2 + 1
            if S[len(S) - 1 - i] == C: diff2, res[len(S) - 1 - i], char2 = 0, 0, True
        return res

    def shortestToChar2(self, s: str, c: str) -> List[int]:
        position_map = defaultdict(list)
        res = [-1] * len(s)
        for i, ch in enumerate(s):
            position_map[ch].append(i)
        for i in range(len(s)):
            res[i] = min(map(lambda x: abs(x - i),position_map[c]))
        return res


s = "loveleetcode"
c = "e"
Solution().shortestToChar2(s, c)
