class Solution:
    def dp(self,n,dp):
        if dp[n]:
            return dp[n]

        if n == 0 or n == 1:
            return 1

        sum = 0
        for i in range(1,n+1):
            sum += self.dp(i-1,dp) * self.dp(n-i,dp)

        dp[n] = sum
        return sum


    def Solve(self,A):
        dp = [0 for _ in range(A + 1)]
        return self.dp(A,dp)

    def uniqueBST(self,A):
        dp = [0 for _ in range(A + 1)]
        dp[0] = 1
        for i in range(1, A + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[-1]


if __name__ == '__main__':
    A = 4
    B = Solution()
    print(B.Solve(A))
    print(B.uniqueBST(A))
