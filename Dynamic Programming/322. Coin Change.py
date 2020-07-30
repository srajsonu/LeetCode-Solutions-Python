class Solution:
    def dp(self,coins,rem, dp):
        if rem < 0: return -1

        if rem == 0: return 0

        if dp[rem]: return dp[rem]

        min_ = float('inf')
        for coin in coins:
            ans = self.dp(coins, rem-coin, dp)
            if ans >= 0 and ans < min_:
                min_ = 1 + ans

        dp[rem] = min_
        return min_

    def Solve(self,A, B):
        dp = [0 for _ in range(B+1)]
        return self.dp(A,B,dp), dp

    def coinChange(self,coins,amount):
        n = len(coins)
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0

        for i in range(1,amount+1):
            for j in range(n):
                if A[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)
                    print(dp[i])

        return dp[-1] if dp[-1] != float('inf') else -1


if __name__ == '__main__':
    A = [1,2,5]
    B = 11
    C = Solution()
    print(C.Solve(A, B))
    print(C.coinChange(A,B))
