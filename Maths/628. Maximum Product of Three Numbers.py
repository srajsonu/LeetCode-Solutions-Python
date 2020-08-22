from heapq import *
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        heapify(nums)
        tmp1 = nlargest(3, nums)
        tmp2 = nsmallest(2, nums)

        return max(tmp1[0] * tmp1[1] * tmp1[2], tmp2[0] * tmp2[1] * tmp1[0])
