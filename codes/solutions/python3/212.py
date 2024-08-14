class Solution:
    def findWords(self, board, words):
        def explore(i, j, cur):
            visited[i][j] = 0
            if "#" in cur and cur["#"] not in res_set: res.append(cur["#"]); res_set.add(cur["#"])
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and board[x][y] in cur and visited[x][y] == -1: explore(x, y, trie[
                    cur[board[x][y]]])
            visited[i][j] = -1

        trie, cnt, m, n, res, res_set = {}, 1, len(board), len(board and board[0]), [], set()
        visited, trie[0] = [[-1] * n for _ in range(m)], {}
        for w in words:
            cur = trie[0]
            for c in w:
                if c not in cur: trie[cnt], cur[c], cnt = {}, cnt, cnt + 1
                cur = trie[cur[c]]
            cur["#"] = w
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie[0]: explore(i, j, trie[trie[0][board[i][j]]])
        return res

    def findWords1(self, board, words):

        def dfs(i, j, w, k):
            if k == len(w) or w[k:] in trie: return True
            if (i, j) not in visited and 0 <= i < len(board) and 0 <= j < len(board and board[0]) \
                    and board[i][j] == w[k]:
                trie.add(w[:k + 1])
                visited.add((i, j))
                for u, v in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    if dfs(i + u, j + v, w, k + 1):
                        return True
                visited.remove((i, j))
            return False

        out = []
        trie = set()
        for w in words:
            visited = set()
            for i in range(len(board)):
                for j in range(len(board and board[0])):
                    if dfs(i, j, w, 0):
                        out.append(w)
        print(list(set(out)))
        return list(set(out))


board = [["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]]
words = ["oa", "oaa"]
Solution().findWords1(board, words)
