from typing import List


class NumMatrix:

    def __init__(self, matrix):
        self.sums = [[0] * (len(matrix and matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix and matrix[0])):
                self.sums[i + 1][j + 1] = self.sums[i][j + 1] + self.sums[i + 1][j] - self.sums[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        return self.sums[row2 + 1][col2 + 1] - self.sums[row2 + 1][col1] - self.sums[row1][col2 + 1] + self.sums[row1][
            col1]


class NumMatrix1:

    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.sum_matrix = [[0 for _ in range(self.m)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if j - 1 >= 0:
                    self.sum_matrix[i][j] += self.sum_matrix[i][j - 1]
                self.sum_matrix[i][j] += matrix[i][j]
        for i in range(self.m):
            for j in range(self.n):
                if j - 1 >= 0:
                    self.sum_matrix[j][i] += self.sum_matrix[j - 1][i]
        print(self.sum_matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a, b, c = 0, 0, 0
        if row1 - 1 >= 0:
            a = self.sum_matrix[row1 - 1][col2]
        if col1 - 1 >= 0:
            b = self.sum_matrix[row2][col1 - 1]
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            c = self.sum_matrix[row1 - 1][col1 - 1]
        return self.sum_matrix[row2][col2] - a - b + c


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
m = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]

obj = NumMatrix1(m)
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
