class Solution:
    def dp(self,A,i,dp):
        global ans
        if dp[i] != float('inf'):
            return dp[i]

        if i < 0:
            ans = 0
        else:
            ans = min(self.dp(A,i-1,dp), self.dp(A,i-2,dp)) + A[i]

        dp[i] = ans
        return ans

    def Solve(self,A):
        n = len(A)
        dp = [float('inf') for _ in range(n)]
        self.dp(A,n-1,dp)
        return min(dp[-1],dp[-2])

if __name__ == '__main__':
    A = [10, 15, 20]
    B = Solution()
    print(B.Solve(A))
