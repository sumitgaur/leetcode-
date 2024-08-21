class Solution:
    def exist(self, board, word):
        m, n, o = len(board), len(board and board[0]), len(word)

        def explore(i, j, k, q):
            for x, y in ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)):
                if k >= o or (0 <= x < m and 0 <= y < n and board[x][y] == word[k] and (x, y) not in q and explore(x, y,
                                                                                                                   k + 1,
                                                                                                                   q | {
                                                                                                                       (
                                                                                                                               x,
                                                                                                                               y)})): return True
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and explore(i, j, 1, {(i, j)}): return True
        return False

    def exist1(self, board, word: str) -> bool:
        def dfs(s, i, j):
            if not s:
                return True
            if (
                    0 <= i < len(board)
                    and 0 <= j < len(board[0])
                    and (i, j) not in visited
                    and s[0] == board[i][j]
            ):
                visited.add((i, j))
                for x, y in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    if dfs(s[1:], i + x, j + y):
                        return True
                visited.remove((i,j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if dfs(word, i, j):
                    return True
        return False


board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
word = "SEEEFS"
print(Solution().exist1(board, word))
