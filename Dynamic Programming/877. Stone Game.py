class Solution:
    def dp(self, A, i, j, dp):
        global ans
        if dp[i][j]:
            return dp[i][j]
        elif i == j:
            ans = A[i]
        else:
            a = self.dp(A, i + 1, j, dp) - A[i]
            b = self.dp(A, i, j - 1, dp) - A[j]
            ans = max(a, b)

        dp[i][j] = ans
        return ans

    def stoneGame(self, A):
        m = len(A)
        dp = [[0] * m for _ in range(m)]
        return True if self.dp(A, 0, m - 1, dp) else False
