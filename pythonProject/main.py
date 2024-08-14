import sys


def nearest(grid):
    visited = set()
    dist = [[sys.maxsize] * len(grid[0]) for _ in range(len(grid))]

    def do(grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            visited.add((i, j))
            if grid[i][j] == 1:
                dist[i][j] = 0
                return 0

            for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (i + a, j + b) not in visited:
                    dist[i][j] = min(dist[i][j], do(grid, i + a, j + b) + 1)
                else:
                    dist[i][j] = min(dist[i][j], dist[i + a][j + b] + 1)
            return dist[i][j]
        return sys.maxsize

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited:
                do(grid, i, j)
    return dist


# {
# Driver Code Starts
if __name__ == '__main__':
    grid = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 0]]
    print(nearest(grid))
# } Driver Code Ends
