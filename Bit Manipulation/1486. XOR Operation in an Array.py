from functools import reduce
from operator import ixor


class Solution:
    def xorOperation(self, n: int, s: int):
        ans = 0
        i = 0
        while i < n:
            ans ^= (s + 2*i)
            i += 1

        return ans
