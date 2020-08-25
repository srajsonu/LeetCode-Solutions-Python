from heapq import *
from typing import List


class Solution:
    def countBits(self, n):
        cnt = 0
        while n:
            n &= n - 1
            cnt += 1
            n >>= 1
        return cnt

    def countBits2(self, n):
        cnt = 0
        for i in range(32):
            cnt += n & 1
            n >>= 1
        return cnt

    def sortByBits(self, arr: List[int]) -> List[int]:
        ans = []
        for num in arr:
            ones = self.countBits(num)
            ans.append((ones, num))
        heapify(ans)
        res = []
        while ans:
            res.append(heappop(ans)[1])

        return res
