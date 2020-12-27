class Solution:
    def dp(self, s, i, j, dp):
        ans = False
        if i >= j:
            return True

        if dp[i][j]:
            return dp[i][j]

        if s[i] == s[j]:
            ans = self.dp(s, i+1, j-1, dp)

        dp[i][j] = ans
        return ans


    def countSubstrings(self, s):
        cnt = 0
        n = len(s)
        dp = [[False]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(i, n):
                if self.dp(s, i, j, dp):
                    cnt += 1

        return cnt

    def solve(self, s):
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        cnt = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1

                elif i + 1 == j:
                    dp[i][j] = 1 if s[i] == s[j] else 0

                else:
                    dp[i][j] = dp[i+1][j-1] if s[i] == s[j] else 0

                cnt += dp[i][j]

        return cnt


if __name__ == '__main__':
    s = 'abc'
    t = Solution()
    print(t.solve(s))
