from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        a, b = 0, 0
        mask = 1
        while mask & xor == 0:
            mask <<= 1

        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num

        return [a, b]
