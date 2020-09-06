class Solution:
    def diagonalSum(self, A):
        if not A: return 0
        m = len(A)
        n = len(A[0])
        sm = 0

        i = 0
        j = 0

        while i < m and j < n:
            sm += A[i][j]
            i += 1
            j += 1

        i = 0
        j = n - 1

        while i < m and j >= 0:
            sm += A[i][j]
            i += 1
            j -= 1

        return sm - A[m // 2][n // 2] if m % 2 != 0 else sm
