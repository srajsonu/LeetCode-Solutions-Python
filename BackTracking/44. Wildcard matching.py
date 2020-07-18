class Solution:
    def dp(self,A,B,i,j,aux):
        global ans
        if i == 0 and j == 0:
            return 1

        if A[i-1] == B[j-1] or B[j-1] == '*':
            ans = self.dp(A,B,i-1,j-1,aux)
        elif B[j-1] == '?':
            ans = self.dp(A,B,i-1,j-1,aux)
        return ans

    def Solve(self,A, B):
        m = len(A)
        n = len(B)
        return self.dp(A,B,m-1,n-1,[])

if __name__ == '__main__':
    A = 'aa'
    B = '*'
    C = Solution()
    print(C.Solve(A,B))
