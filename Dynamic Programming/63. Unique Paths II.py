class Solution:
    def dp(self,A,i,j,dp):
        global ans
        if dp[i][j]:
            return dp[i][j]

        if i == 0 and j == 0:
            ans = 1

        elif A[i][j] == 1:
            ans = 0
        elif i == 0 or j == 0:
            if  i == 0:
                ans = self.dp(A,i,j-1,dp)
            else:
                ans = self.dp(A,i-1,j,dp)
        else:
            ans = self.dp(A,i-1,j,dp) + self.dp(A,i,j-1,dp)

        dp[i][j] = ans
        return ans

    def Solve(self,A):
        m = len(A)
        n = len(A[0])
        dp = [[0]*n for _ in range(m)]
        self.dp(A,m-1,n-1,dp)
        return dp

if __name__ == '__main__':
    A = [[0,0,0],
         [0,1,0],
         [0,0,0]]

    C = [[0,0],[1,1],[0,0]]

    B = Solution()
    print(B.Solve(C))
