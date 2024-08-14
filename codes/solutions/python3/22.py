from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        bfs = [(0, 0, '')]
        for c in range(n * 2):
            bfs = [(l + 1, r, s + '(') for l, r, s in bfs if l + 1 <= n] + [(l, r + 1, s + ')') for l, r, s in bfs if
                                                                            l - r]
        return [s for l, r, s in bfs]


for i in range(1, 10):
    parenthesis = Solution().generateParenthesis(i)
    print(parenthesis, len(parenthesis))
