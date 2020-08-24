from typing import List


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        n = len(A)
        r = curr_sum = sum(i * j for i, j in enumerate(A))
        s = sum(A)

        while A:
            curr_sum += s - A.pop() * n
            r = max(r, curr_sum)

        return r
