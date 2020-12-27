class Solution:
    def countVowelStrings(self, n):
        m = 5
        dp = [[0]*m for _ in range(n)]

        for i in range(n):
            dp[i][-1] = 1

        tmp = 1
        for i in reversed(range(m)):
            dp[0][i] = tmp
            tmp += 1

        for i in range(1, n):
            for j in reversed(range(m-1)):
                dp[i][j] = dp[i-1][j] + dp[i][j+1]

        return dp[-1][0]

if __name__ == '__main__':
    A = 33
    B = Solution()
    print(B.countVowelStrings(A))
