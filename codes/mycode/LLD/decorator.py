from time import time


def timeit(func):
    def wrapper_function(*args, **kwargs):
        s = time()
        res = func(*args, **kwargs)
        e = time()
        print(f"time take to execute {func.__name__}: {e - s}")
        return res

    return wrapper_function


@timeit
def print_xyz(x):
    return (f"XYZ{x}")


print(print_xyz("I am decorated"))
