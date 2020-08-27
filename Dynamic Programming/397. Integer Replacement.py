class Solution:
    def dfs(self, n, dp):
        global ans
        if n in dp:
            return dp[n]

        if n == 1:
            return 0

        if n % 2 == 0:
            ans = 1 + self.dfs(n // 2, dp)
        else:
            ans = 1 + min(self.dfs(n + 1, dp), self.dfs(n - 1, dp))

        dp[n] = ans
        return ans

    def integerReplacement(self, n: int) -> int:
        dp = {}
        return self.dfs(n, dp)
