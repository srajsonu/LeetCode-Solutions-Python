from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(32):
            cnt = 0
            for j in range(n):
                if (nums[j] >> i) & 1:
                    cnt += 1
            total += cnt * (n - cnt)

        return total
