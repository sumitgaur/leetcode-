from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix and matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float("inf")
                    if i > 0 and matrix[i - 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i - 1][j] + 1
                    if j > 0 and matrix[i][j - 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j - 1] + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    if i + 1 < m and matrix[i + 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i + 1][j] + 1
                    if j + 1 < n and matrix[i][j + 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j + 1] + 1
        return matrix
    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1

        while q:
            i, j = q.popleft()
            for h, v in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i + h < len(mat) and 0 <= j + v < len(mat[0]) and mat[i + h][j + v] == -1:
                    mat[i + h][j + v] = mat[i][j] + 1
                    q.append((i + h, j + v))
        return mat


mat = [[0,0,0],[0,1,0],[1,1,1]]
print(Solution().updateMatrix2(mat))
