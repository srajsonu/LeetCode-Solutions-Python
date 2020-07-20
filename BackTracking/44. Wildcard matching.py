class Solution:
    def dp(self,A,B,i,j,aux):
        if aux[i][j] != -1:
            return aux[i][j]
        ans = 0
        if i == 0 and j == 0:
            ans = 1

        elif j == 0:
            ans = 0

        elif i == 0:
            if B[j-1] == '*':
                ans = self.dp(A,B,i,j-1,aux)

        elif A[i-1] == B[j-1] or B[j-1] == '?':
            ans =  self.dp(A,B,i-1,j-1,aux)

        elif B[j-1] == '*':
            ans = self.dp(A,B,i-1,j,aux) or self.dp(A,B,i,j-1,aux)
        else:
            ans = 0
        aux[i][j] = ans
        return ans

    def Solve(self,A, B):
        A = '_'+A
        B = '_'+B
        m = len(A)
        n = len(B)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        return self.dp(A,B,m,n,dp)

if __name__ == '__main__':
    A = 'acdcb'
    B = 'a*c?b'
    C = Solution()
    print(C.Solve(A,B))
