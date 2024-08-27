def partition(arr, l, r):
    x = arr[r]
    i = l
    while l < r:
        if arr[l] <= x:
            arr[l], arr[i] = arr[i], arr[l]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def quick_select(arr, k, l, r):
    pivot_in = partition(arr, l, r)
    if pivot_in - l == k - 1:
        return arr[pivot_in]
    if pivot_in - l > k - 1:
        return quick_select(arr, l, pivot_in - 1, k)
    return quick_select(arr, pivot_in + 1, r, k - pivot_in + l - 1)
