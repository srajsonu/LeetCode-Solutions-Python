class Solution:
    def dp(self, A, i, dp):
        if dp[i]:
            return dp[i]

        if i == 0:
            return 1

        s = len(A) - i
        if A[s] == '0':
            return 0

        ans = self.dp(A,i-1,dp)

        if i >= 2 and int(A[s:s+2]) <= 26:
            ans += self.dp(A,i-2,dp)

        dp[i] = ans
        return ans

    def Solve(self, A):
        n = len(A)
        dp = [0 for _ in range(n + 1)]
        self.dp(A, n, dp)
        return dp

    def numDecodings(self,A):
        n = len(A)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1 if A[0] != '0' else 0

        for i in range(2,n+1):
            first = int(A[i-1:i])
            second = int(A[i-2:i])

            if first >= 1 and first <= 9:
                dp[i] += dp[i-1]

            if second >= 10 and second <= 26:
                dp[i] += dp[i-2]

        return dp[-1]

if __name__ == '__main__':
    A = "226"
    B = Solution()
    print(B.Solve(A))
    print(B.numDecodings(A))
