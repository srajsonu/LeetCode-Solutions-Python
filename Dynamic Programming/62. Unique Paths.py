class Solution:
    def dp(self,A,i,j,dp):
        global ans
        if dp[i][j]:
            return dp[i][j]

        if i == 0 or j == 0:
            ans = 1
        else:
            ans = self.dp(A,i-1,j,dp) + self.dp(A,i,j-1,dp)
        dp[i][j] = ans
        return ans

    def Solve(self,m,n):
        dp = [[0]*n for _ in range(m)]
        self.dp(A,m-1,n-1,dp)
        return dp[-1][-1]

if __name__ == '__main__':
    A = 3
    B = 2
    C = Solution()
    print(C.Solve(A,B))
