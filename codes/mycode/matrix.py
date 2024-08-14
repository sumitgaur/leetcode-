def isToeplitzMatrix(matrix):
    def do(matrix, i, j, x):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
            if matrix[i][j] == x:
                return do(matrix, i + 1, j + 1, x)
            else:
                return False
        else:
            return True

    for i in range(len(matrix)):
        if not do(matrix, i, 0, matrix[i][0]):
            return False
    for j in range(len(matrix)):
        if not do(matrix, 0, j, matrix[0][j]):
            return False
    return True


m = [[1, 2], [2, 2]]
isToeplitzMatrix(m)
