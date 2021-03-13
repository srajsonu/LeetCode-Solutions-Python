class Solution:
    def dp(self, A, i, j, dp):
        global ans
        if dp[i][j]:
            return dp[i][j]
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[i]):
            return 0

        if A[i][j] == '0':
            ans = 0
        else:
            ans = 1 + min(self.dp(A, i-1, j, dp), self.dp(A, i, j-1, dp), self.dp(A, i-1, j-1, dp))

        dp[i][j] = ans
        return ans

    def maximalSquare(self, A):
        m = len(A)
        n = len(A[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == '1':
                    ans = max(ans, self.dp(A, i, j, dp))

        return ans ** 2


if __name__ == '__main__':
    A = [["1", "0", "1", "0", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "0", "0", "1", "0"]]

    B = Solution()
    print(B.maximalSquare(A))
