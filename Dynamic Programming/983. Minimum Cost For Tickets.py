class Solution:
    def dp(self, A, B, i, dp):
        if dp[i] != -1:
            return dp[i]

        if i == len(A):
            return 0

        ans = float('inf')
        ans = min(self.dp(A, B, i + 1, dp) + B[0], ans)

        j = i
        while j < len(A) and A[j] < A[i] + 7:
            j += 1

        ans = min(self.dp(A, B, j, dp) + B[1], ans)

        j = i
        while j < len(A) and A[j] < A[i] + 30:
            j += 1

        ans = min(self.dp(A, B, j, dp) + B[2], ans)

        dp[i] = ans
        return ans

    def mincostTickets(self, A, B) -> int:
        n = len(A)
        dp = [-1 for _ in range(n + 1)]
        return self.dp(A, B, 0, dp)
