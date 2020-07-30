from math import sqrt
import sys
sys.setrecursionlimit(10**9)

class Solution:
    def dp(self,n,dp):
        if dp[n]:
            return dp[n]

        if n < 4:
            return n

        count = float('inf')
        for i in range(1, int(sqrt(n))+1):
            count = min(count, self.dp(n - i*i, dp) + 1)
            i += 1

        dp[n] = count
        return count

    def Solve(self,n):
        dp = [0 for _ in range(n+1)]
        return self.dp(n,dp)

    def numSquares(self,n):
        if n < 4:
            return n

        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for i in range(4,n+1):
            for j in range(1,int(sqrt(i))+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[-1]

if __name__ == '__main__':
    A = 8441
    B = Solution()
    print(B.Solve(A))
    print(B.numSquares(A))
