def find_largest_in_list(arr):
    return max(arr)


def sort_based_on_square(arr):
    return sorted(arr, key=lambda x: x * x)


def get_numpy_identity_matrix(size):
    import numpy as np
    return np.identity(size)


assert find_largest_in_list([2, -1, -5, 2, 4]) == 4
assert sort_based_on_square([2, -1, -5, 2, 4]) == [-1, 2, 2, 4, -5]
assert get_numpy_identity_matrix(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
