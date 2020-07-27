class Solution:
    def dp(self,A,dp):
        if dp[A]:
            return dp[A]
        global ans
        if A <= 2:
            ans = A
        else:
            ans = self.dp(A-1,dp) + self.dp(A-2,dp)
        dp[A] = ans
        return ans

    def Solve(self,A):
        dp = [0 for _ in range(A+1)]
        self.dp(A,dp)
        return dp[-1]

if __name__ == '__main__':
    A = 6
    B = Solution()
    print(B.Solve(A))
