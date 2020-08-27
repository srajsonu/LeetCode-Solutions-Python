from typing import List


class Solution:
    def maxAbsValExpr(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        row = [1, 1, -1, -1]
        col = [1, -1, 1, -1]
        res = 0
        for r, c in zip(row, col):
            smallest = r * A[0] + c * B[0] + 0

            for i in range(n):
                cur = r * A[i] + c * B[i] + i
                res = max(res, cur - smallest)
                smallest = min(smallest, cur)

        return res
