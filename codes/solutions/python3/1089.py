from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        for num in list(arr):
            if i >= len(arr): break
            arr[i] = num
            if not num:
                i += 1
                if i < len(arr):
                    arr[i] = num
            i += 1

    def duplicateZeros2(self, arr):
        zeroes = arr.count(0)
        i = len(arr) - 1
        n = len(arr)
        while i >= 0:
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0
            i -= 1


l = [1, 0, 2, 3, 0, 4, 5, 0]
Solution().duplicateZeros2(l)
print(l)
