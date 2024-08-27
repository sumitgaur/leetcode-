# given NXN chess board and initial position of knight and bishop
# your are given final position of knight as well, find the min steps requird by knight to reach the final position
# without crossing bishop's path, or knight can kill the bishop as well

from collections import deque


def min_steps(N, kx, ky, bx, by, fkx, fky):
    def is_safe_move(x, y, iba):
        if 0 <= x < N and 0 <= y < N:
            return (not iba) or (abs(bx - by))  # not blocked by bishop

    bfs = deque()
    is_bishop_alive = True
    visited = set()
    bfs.append([(kx, ky), 0, is_bishop_alive,1])
    while len(bfs):
        (kx, ky), steps, iba = bfs.popleft()
        if (kx, ky) == (fkx, fky):
            return steps
        if (kx, ky) == (bx, by):
            iba = False  # killed bishop
        for i, j in [(-2, 1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, -1), (2, -1)]:
            if is_safe_move(kx + i, ky + j, iba):
                bfs.append([(kx + i, ky + j), steps + 1, iba,1])

    return None
