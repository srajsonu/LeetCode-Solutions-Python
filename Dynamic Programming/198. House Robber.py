class Solution:
    def dp(self,A,i,dp):
        global ans
        if dp[i]:
            return dp[i]

        if i == 0:
            ans = A[i]
        elif A[i] == 0:
            ans = self.dp(A,i-1,dp)
        elif i == 1:
            ans = max(A[i],A[i-1])
        else:
            ans = max(self.dp(A,i-1,dp), self.dp(A,i-2,dp)+A[i])

        dp[i] = ans
        return ans

    def Solve(self,A):
        n = len(A)
        dp = [0 for _ in range(n)]
        self.dp(A,n-1,dp)
        return dp[-1]

    def rob(self,nums):
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]



if __name__ == '__main__':
    A = [1,2,3,1]
    B = Solution()
    print(B.Solve(A))
    print(B.rob(A))
