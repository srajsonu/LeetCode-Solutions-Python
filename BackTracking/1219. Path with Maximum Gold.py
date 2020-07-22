class Solution:
    def dfs(self,A,i,j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] == 0:
            return 0

        tmp = A[i][j]
        A[i][j] = 0
        row = [1,0,-1,0]
        col = [0,1,0,-1]
        ans = 0
        for r,c in zip(row,col):
            ans = max(ans,self.dfs(A,i+r,j+c))
        A[i][j] = tmp
        return ans + tmp

    def Solve(self,A):
        m = len(A)
        n = len(A[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    ans = max(ans,self.dfs(A,i,j))
        return ans


if __name__ == '__main__':
    A = [[0, 6, 0],
         [5, 8, 7],
         [0, 9, 0]]
    B = Solution()
    print(B.Solve(A))
