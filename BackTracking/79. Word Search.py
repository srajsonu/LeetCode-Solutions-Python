class Solution:
    def dfs(self,A,B,i,j,index):
        if index == len(B):
            return True

        if i < 0 or i >= self.m or j < 0 or j >= self.n or B[index] != A[i][j]:
            return False

        tmp = A[i][j]
        A[i][j] = "#"

        ans = self.dfs(A,B,i+1,j,index+1) or\
              self.dfs(A,B,i,j+1,index+1) or\
              self.dfs(A,B,i-1,j,index+1) or\
              self.dfs(A,B,i,j-1,index+1)

        A[i][j] = tmp

        return ans


    def Solve(self,A,B):
        self.m = len(A)
        self.n = len(A[0])
        self.ans = 0
        #vis = [[False]*n for _ in range(m)]
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(A,B,i,j,0):
                    return True
        return False


if __name__ == '__main__':
    A = [['A','B','C','E'],
         ['S','F','C','S'],
         ['A','D','E','E']]
    B = 'ABCC'
    C = Solution()
    print(C.Solve(A,B))
