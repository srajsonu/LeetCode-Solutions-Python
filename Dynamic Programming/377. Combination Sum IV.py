class Solution:
    def dp(self,A,B,dp):
        if dp[B] != -1:
            return dp[B]

        ans = 0
        for i in range(len(A)):
            if A[i] <= B:
                ans += self.dp(A,B-A[i],dp)

        dp[B] = ans
        return ans

    def Solve(self,A, B):
        dp = [-1 for _ in range(B+1)]
        dp[0] = 1
        return self.dp(A,B,dp)

    def combinationSum4(self,A,B):
        n = len(A)
        dp =[0 for _ in range(B+1)]
        dp[0] = 1
        for i in range(1,B+1):
            for j in range(n):
                if i - A[j] >= 0:
                    dp[i] += dp[i-A[j]]
        return dp[-1]

if __name__ == '__main__':
    A = [1, 2, 3]
    B = 4
    C = Solution()
    print(C.Solve(A, B))
    print(C.combinationSum4(A,B))
