class Solution:
    def LIS(self,A):
        n = len(A)
        dp = [1 for _ in range(n)]
        maxx = 1

        for i in range(1,n):
            for j in range(i):
                if A[i] % A[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)
                    maxx = max(maxx,dp[i])

        return maxx, dp

    def Solve(self,A):
        n = len(A)
        ans = []
        A.sort()
        maxx, dp = self.LIS(A)
        prev = -1

        for i in reversed(range(n)):
            if dp[i] == maxx and (prev % A[i] == 0 or prev == -1):
                ans.append(A[i])
                maxx -= 1
                prev = A[i]

        return ans

if __name__ == '__main__':
    A = [1,2,4,8]
    B = Solution()
    print(B.Solve(A))
