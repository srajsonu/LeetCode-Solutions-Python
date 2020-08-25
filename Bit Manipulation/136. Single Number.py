from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = reduce(lambda x, y: x ^ y, nums)
        return res

    def solve(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans
