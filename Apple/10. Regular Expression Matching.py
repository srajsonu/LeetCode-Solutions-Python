class Solution:
    def dp(self,A,B,i,j,aux):
        global ans
        if aux[i][j]:
            return aux[i][j]
        if i == 0 and j == 0:
            return 1
        if i == 0 or j == 0:
            if j == 0:
                return 0
            else:
                while j-1 and B[j-1] == '*':
                    j-=2
                if j == 0:
                    return 1
                else:
                    return 0

        if A[i-1] == B[j-1] or B[j-1] == '.':
            ans = self.dp(A,B,i-1,j-1,aux)
        elif B[j-1] == '*':
            ans = self.dp(A,B,i,j-2,aux)
        else:
            if A[i-1] == B[j-2] or B[j-2] == '.':
                ans = self.dp(A,B,i,j-1,aux) or self.dp(A,B,i-1,j,aux)
            else:
                ans = self.dp(A,B,i-1,j,aux)
        aux[i][j] = ans
        return ans

    def isMatch(self,A,B):
        A='_'+A
        B='_'+B
        m=len(A)
        n=len(B)
        dp=[[0]*(n+1) for _ in range(m+1)]
        self.dp(A,B,m,n,dp)
        return dp[m][n]
