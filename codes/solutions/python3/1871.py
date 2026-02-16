from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        bfs = deque([0])
        visited,mx = set([0]),0
        while bfs:
            i = bfs.popleft()
            for j in range(max(i+minJump,mx), min(len(s) - 1, i + maxJump) + 1):
                if s[j] == "0" and j not in visited:
                    if j == len(s) - 1:
                        return True
                    bfs.append(j)
                    visited.add(j)
            mx = max(mx,i+maxJump)
        return False



s = "01101110"
minJump = 2
maxJump = 3
res = Solution().canReach(s, minJump, maxJump)
print(res)
