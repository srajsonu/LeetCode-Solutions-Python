class Solution:
    def dp(self, A, i, j, dp):
        global ans
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return float('inf')

        if dp[i][j] != -1:
            return dp[i][j]

        if i == len(A) - 1:
            ans = A[i][j]
        else:
            a = self.dp(A, i + 1, j, dp)
            b = self.dp(A, i + 1, j - 1, dp)
            c = self.dp(A, i + 1, j + 1, dp)
            ans = min(a, b, c) + A[i][j]

        dp[i][j] = ans
        return ans

    def minFallingPathSum(self, A) -> int:
        if not A: return 0
        m = len(A)
        n = len(A[0])
        dp = [[-1] * n for _ in range(m)]
        ans = float('inf')

        for col in range(n):
            tmp = self.dp(A, 0, col, dp)
            ans = min(ans, tmp)

        return ans
