class Solution:
    def dp(self,A,B,i,j,dp):
        global ans
        if dp[i][j]:
            return dp[i][j]

        if i == -1:
            return True

        if j == -1 and i != -1:
            return False

        if A[i] == B[j]:
            ans = self.dp(A,B,i-1,j-1,dp)

        elif A[i] != B[j]:
            ans = self.dp(A,B,i,j-1,dp)

        dp[i][j] = ans
        return ans

    def Solve(self,A,B):
        if len(A) == 0: return True
        if len(B) == 0: return False
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
