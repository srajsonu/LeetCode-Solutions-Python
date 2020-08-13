class Solution:
    def __init__(self, A):
        self.A = A

    def dp(self, A, i, j, dp):
        global ans
        if dp[i][j]:
            return dp[i][j]

        if i == 0 or j == 0:
            ans = 0
        else:
            ans = self.dp(A, i - 1, j, dp) + self.dp(A, i, j - 1, dp) + A[i - 1][j - 1] - self.dp(A, i - 1, j - 1, dp)

        dp[i][j] = ans
        return ans

    def sumRegion(self, row1, col1, row2, col2, dp):
        return dp[row2][col2] - dp[row1 - 1][col2] - dp[row2][col1 - 1] + dp[row1 - 1][col1 - 1]

    def Solve(self, A):
        m = len(A)
        n = len(A[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        self.dp(A, m, n, dp)
        return dp


if __name__ == '__main__':
    A = [[3, 0, 1, 4, 2],
         [5, 6, 3, 2, 1],
         [1, 2, 0, 1, 5],
         [4, 1, 0, 1, 7],
         [1, 0, 3, 0, 5]]

    C = [[2, 0, -3, 4],
         [6, 3, 2, -1],
         [5, 4, 7, 3],
         [2, -6, 8, 1]]

    B = Solution(C)
    print(B.Solve(C))
