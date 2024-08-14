class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        arr = sorted(nums1 + nums2)
        if len(arr) % 2 == 0:
            return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
        else:
            return arr[len(arr) // 2]


def merge(A, B):
    i, j = 0, 0
    res = []
    while i < len(A) and j < len(B):
        if A[i]<B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
    return res+A[i:]+B[j:]


merge([0,0], [0,0])
