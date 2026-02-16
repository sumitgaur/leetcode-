from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue, level, visited = [entrance], 0, {tuple(entrance)}

        while queue:
            l = []
            for a, b in queue:
                for dira, dirb in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    i, j = a + dira, b + dirb
                    if 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] != '+' and (i, j) not in visited:
                        visited.add((i, j))
                        if i == 0 or j == 0 or i == len(maze) - 1 or j == len(maze[0]) - 1:
                            return level + 1
                        l.append([i, j])
            level += 1
            queue = l
        return -1


maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]

print(Solution().nearestExit(maze, entrance))
