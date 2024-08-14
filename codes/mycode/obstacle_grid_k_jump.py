#!/bin/python3

import math
import os
import random
import re
import sys


def getMinimumMoves(maze, k):
    visited = set()
    def do(i, j):
        if not (0 <= i < len(maze) and 0 <= j < len(maze[0])) or (i, j) in visited or maze[i][j] == 1:
            return sys.maxsize
        visited.add((i, j))

        if i == len(maze) - 1 and j == len(maze[0]) - 1:
            visited.remove((i, j))
            return 0
        res = sys.maxsize
        for x in range(1, k + 1):
            res = min(res,
                      min(do(i + x, j), do(i - x, j), do(i, j + x), do(i, j - x)) + 1
                      )
        visited.remove((i, j))
        return res

    return do(0, 0)


if __name__ == '__main__':
    maze = [[0, 0, 0], [1, 0, 0]]
    k = 3
    print(getMinimumMoves(maze, k))
