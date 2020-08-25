from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        missing = set(nums)
        for i in range(n):
            if i not in missing:
                return i
