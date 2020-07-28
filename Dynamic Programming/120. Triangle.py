class Solution:
    def dp(self,A,row,col,dp):
        global ans
        if dp[row][col]:
            return dp[row][col]

        if row < 0 or row >= len(A) or col < 0 or col >= len(A[row]):
            return 0

        if row == len(A):
            ans = A[row][col]
        else:
            ans = min(self.dp(A,row+1,col, dp), self.dp(A,row+1,col+1, dp)) + A[row][col]

        dp[row][col] = ans
        return ans

    def Solve(self,A):
        m = len(A)
        n = len(A[-1])
        dp = [[0]*(n+1) for _ in range(m+1)]
        return self.dp(A,0,0,dp)

    def minimumTotal(self,triangle):
        m = len(triangle)
        dp = triangle[-1]
        for i in reversed(range(m-1)):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j],dp[j+1]) + triangle[i][j]

        return dp[0]

if __name__ == '__main__':
    A = [[2],
        [3,4],
       [6,5,7],
      [4,1,8,3]]

    B = Solution()
    print(B.Solve(A))
    print(B.minimumTotal(A))
