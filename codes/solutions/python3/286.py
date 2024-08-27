class Solution:
    def wallsAndGates(self, rooms):
        m, n = len(rooms), len(rooms and rooms[0])
        q, dist = [(i, j) for i in range(m) for j in range(n) if not rooms[i][j]], 0
        while q:
            new = []
            dist += 1
            for i, j in q:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and rooms[x][y] == 2147483647:
                        rooms[x][y] = dist
                        new.append((x, y))
            q = new

    def wallsAndGates(self, rooms):
        visited = set()

        def dfs(i, j, dist):
            if (i, j) in visited or not (0 <= i < len(rooms) and 0 <= j < len(rooms[0])) or rooms[i][j] < 0:
                return
            visited.add((i, j))
            rooms[i][j] = min(rooms[i][j], dist + 1)
            for u, v in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                dfs(i + u, j + v, dist + 1)
            visited.remove((i, j))

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)
        return rooms
