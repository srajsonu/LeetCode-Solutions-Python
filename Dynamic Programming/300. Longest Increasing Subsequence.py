class Solution:
    def dp(self,A,i,j,aux,dp):
        if i == len(A):
            return j

        ans = j
        min_ = float('inf')
        for k in range(i, len(A)):
            if A[i] > aux and A[i] < min_:
                min_ = A[i]
                tmp = self.dp(A,k+1,j+1,A[i],dp)
                if tmp > ans:
                    ans = tmp

        return ans

    def Solve(self,A):
        n = len(A)
        dp = [1 for _ in range(n+1)]
        return self.dp(A,0,0,float('-inf'),dp)

    def lengthOfLIS(self,A):
        n = len(A)
        if n == 0: return 0
        dp = [1 for _ in range(n+1)]
        for i in range(1,n):
            for j in range(i):
                if A[i] > A[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

if __name__ == '__main__':
    A = [10,9,2,5,3,7,101,18]
    B = Solution()
    print(B.Solve(A))
    print(B.lengthOfLIS(A))
