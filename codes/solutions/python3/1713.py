from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        def lcs(a, b, i, j):
            if i >= 0 and j >= 0:
                if a[i] == b[j]:
                    lcs_arr = lcs(a, b, i - 1, j - 1)
                    return lcs_arr + [a[i]]
                lcs_arr1 = lcs(a, b, i - 1, j)
                lcs_arr2 = lcs(a, b, i, j - 1)
                if len(lcs_arr1) > len(lcs_arr2):
                    return lcs_arr1
                else:
                    return lcs_arr2
            return []

        lcs_arr = lcs(target, arr, len(target) - 1, len(arr) - 1)
        print(lcs_arr)


target = [6, 4, 8, 1, 3, 2]
arr = [4, 7, 6, 2, 3, 8, 6, 1]
Solution().minOperations(target, arr)
