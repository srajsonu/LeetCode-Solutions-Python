class Solution:
    def dp(self, A, i, j, dp):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return 0

        if dp[i][j]:
            return dp[i][j]

        elif A[i][j] == 1:
            ans = min(self.dp(A,i-1,j,dp), self.dp(A,i-1,j-1,dp), self.dp(A,i,j-1,dp)) + 1
            dp[i][j] = ans
            return ans
        else:
            return 0

    def Solve(self, A):
        m = len(A)
        n = len(A[0])
        dp = [[0]*n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    ans = max(ans, self.dp(A,i,j,dp))
        return ans ** 2

    def maximalSquare(self, matrix):
        m = len(matrix)
        if m == 1: return max(matrix[0])
        n = len(matrix[0])
        dp = [[0] * (n) for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i-1][j])
                    ans = max(ans, dp[i][j])

        return ans ** 2


if __name__ == '__main__':
    A = [[1, 0, 1, 0, 0],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 0, 0, 1, 0]]

    C = [[0,1],[1,0]]

    B = Solution()
    print(B.Solve(C))
    print(B.maximalSquare(C))
