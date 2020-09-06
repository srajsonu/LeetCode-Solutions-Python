class Solution:
    def countSquares(self, A):
        m = len(A)
        n = len(A[0])

        ans = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    if i == 0 or j == 0:
                        ans += 1
                    else:
                        val = min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + A[i][j]
                        ans += val
                        A[i][j] = val

        return ans
