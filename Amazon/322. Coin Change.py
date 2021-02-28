class Solution:
    def dp(self, A, B, i, dp):
        global ans
        if i < 0:
            return float('inf')

        if B < 0:
            return float('inf')

        if dp[i][B] != -1:
            return dp[i][B]

        if B == 0:
            ans = 0

        elif A[i] > B:
            ans = self.dp(A, B, i-1, dp)
        else:
            take = 1 + self.dp(A, B - A[i], i, dp)
            dont = self.dp(A, B, i-1, dp)
            ans = min(take, dont)

        dp[i][B] = ans
        return ans

    def coinChange(self, A, B):
        n = len(A)
        dp = [[-1 for _ in range(B+1)] for _ in range(n+1)]
        ans = self.dp(A, B, n-1, dp)
        return ans if ans != float('inf') else -1

    def solve(self, A, B):
        n = len(A)
        dp = [float('inf') for _ in range(B + 1)]
        dp[0] = 0

        for i in range(B+1):
            for j in range(n):
                if A[j] <= i:
                    dp[i] = min(dp[i], dp[i-A[j]] + 1)

        return dp[-1]


if __name__ == '__main__':
    A = [1, 2, 5]
    B = 11
    C = Solution()
    print(C.coinChange(A, B))
    print(C.solve(A, B))
