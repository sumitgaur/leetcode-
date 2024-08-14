# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]   all 1s are connected,, so representing a single island
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
#
# Output: 3 // unit length 4,1,2
# grid = [
#   ["1","1","1","0","0"],
#   ["1","0","1","0","0"],
#   ["1","1","1","0","0"],
#   ["0","0","0","1","1"]
# ]

# Output:2
# (0,0)->(0,1)->(0,2)->(1,2)->(2,2)->(2,1)->(2,0)->(1,0)  visited
# (i,j)->

def countIsland(grid):
    visited = set()
    count = 0

    def dfs(grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            visited.add((i, j))
            for x, y in [(i + 1, j), (i - 1, j), (j + 1, i), (j - 1, i)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited and grid[x][y] == "1":
                    dfs(grid, x, y)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] == "1":
                dfs(grid, i, j)
                count += 1
    return count


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
assert countIsland(grid) == 3
