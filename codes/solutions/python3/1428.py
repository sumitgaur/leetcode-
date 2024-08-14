# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
import bisect


class BinaryMatrix(object):
    def __init__(self):
        self.matrix = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]]

    def get(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def dimensions(self) -> list:
        return [len(self.matrix), len(self.matrix and self.matrix[0])]


def leftMostColumnWithOne(binaryMatrix: BinaryMatrix):
    i = 0

    m, n = binaryMatrix.dimensions()
    j = n - 1
    ans = n
    while i < m:
        row_slice = [binaryMatrix.get(i, col) for col in range(j + 1)]
        x = bisect.bisect_left(row_slice, 1)
        ans = min(ans, x + 1)
        j = x
        i += 1
    print(ans)
    return ans


bm = BinaryMatrix()
leftMostColumnWithOne(bm)
