class Solution:
    def dp(self,A,i,dp):
        global ans
        if dp[i]:
            return dp[i]

        if i < 0:
            ans = 0
        elif A[i] == 0:
            ans = self.dp(A,i-1,dp)
        else:
            ans = max(self.dp(A,i-1,dp), self.dp(A,i-2,dp) + A[i])

        dp[i] = ans
        return ans


    def Solve(self,A):
        n = len(A)
        if n <= 1:
            return 0
        dp = [0 for _ in range(n)]
        self.dp(A,n-1,dp)
        return dp[-1]

if __name__ == '__main__':
    A = [1,2,3,4,5]
    B = Solution()
    print(B.Solve(A))
