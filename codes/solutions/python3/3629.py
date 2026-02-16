import math
from typing import List


class Solution:
    def _is_prime(self, n):
        """Checks if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def minJumps(self, nums: List[int]) -> int:
        def do(nums, i):
            if 0 <= i < len(nums):
                if i == len(nums) - 1:
                    return 0
                adj_jump = do(nums, i + 1)
                prime_jump = float('inf')
                if self._is_prime(nums[i]):
                    prime_jump = min(
                        (do(nums, j) for j in range(i + 1, len(nums)) if nums[j] % nums[i] == 0),
                        default=float('inf')
                    )
                return 1 + min(adj_jump, prime_jump)
            return float('inf')

        return do(nums, 0)

nums = [2,3,4,7,9]

print(Solution().minJumps(nums))
