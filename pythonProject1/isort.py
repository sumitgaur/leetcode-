import bisect
def insertionSort(arr):
    # Write your code here
    shifts = 0
    i,j=0,1
    for i, x in enumerate(arr):
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            shifts += 1
            j-=1
        arr[j + 1] = x
    return shifts


insertionSort([2, 1, 3, 1, 2])
