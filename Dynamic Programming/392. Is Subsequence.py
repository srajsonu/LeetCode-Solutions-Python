class Solution:
    def dp(self,A,B,i,j,dp):
        global ans
        if dp[i][j]:
            return dp[i][j]

        if i == 0:
            return True

        if j == 0 and i != 0:
            return False

        if A[i] == B[j]:
            ans = self.dp(A,B,i-1,j-1,dp)

        elif A[i] != B[j]:
            ans = self.dp(A,B,i,j-1,dp)

        dp[i][j] = ans
        return ans

    def Solve(self,A,B):
        if len(A) == 0: return True
        A = '_'+A
        B = '_'+B
        m = len(A)
        n = len(B)
        dp = [[0]*n for _ in range(m)]
        self.dp(A,B,m-1,n-1,dp)
        return dp[-1][-1]

if __name__ == '__main__':
    A = "abc"
    B = "ahbgdc"
    C = Solution()
    print(C.Solve(A,B))
