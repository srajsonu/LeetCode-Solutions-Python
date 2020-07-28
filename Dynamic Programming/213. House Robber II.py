class Solution:
    def dp(self,A,i,j,dp):
        global ans
        if dp[i]:
            return dp[i]

        if A[i] == 0:
            return self.dp(A,i-1,j,dp)

        if j == 0:
            if i == 0:
                ans = A[i]
            elif i == 1:
                ans = max(A[i],A[i-1])
            else:
                ans = max(self.dp(A,i-1,j,dp), self.dp(A,i-2,j,dp) + A[i])
        else:
            if i == 1:
                ans = A[i]
            elif i == 2:
                ans = max(A[i],A[i-1])
            else:
                ans = max(self.dp(A,i-1,j,dp), self.dp(A,i-2,j,dp) + A[i])

        dp[i] = ans
        return ans

    def Solve(self,A):
        n = len(A)
        dp = [0 for _ in range(n)]
        dp1 = [0 for _ in range(n)]
        max1 = self.dp(A,n-1,1,dp)
        max2 = self.dp(A,n-2,0,dp1)
        return max(max1,max2)

    def rob(self,nums):
        n = len(nums)
        if  n == 0:
            return 0

        dp = [0 for _ in range(n)]
        dp1 = [0 for _ in range(n)]

        dp[0] = A[0]
        dp[1] = max(A[0],A[1])

        dp1[1] = A[1]
        dp1[2] = max(A[1],A[2])

        for i in range(2,n-1):
            dp[i] = max(dp[i-1],dp[i-2] + A[i])

        for i in range(3,n):
            dp1[i] = max(dp1[i-1],dp1[i-2] + A[i])

        return max(dp[-2],dp1[-1])

if __name__ == '__main__':
    A = [1,2,1,1]
    B = Solution()
    print(B.Solve(A))
    print(B.rob(A))
