class Solution:
    def maxSumAfterPartitioning(self, A, k: int) -> int:
        n = len(A)
        dp = [0 for _ in range(n + 1)]

        for i in range(n):
            curr_max = 0
            for j in range(1, min(k, i + 1) + 1):
                curr_max = max(curr_max, A[i - j + 1])
                dp[i] = max(dp[i], dp[i - j] + curr_max * j)

        return dp[n - 1]
