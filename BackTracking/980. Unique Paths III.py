class Solution:
    def dfs(self,A,i,j,count):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] == -1:
            return

        if A[i][j] == 2:
            print(count)
            if count == 0:
                self.count += 1
            return

        A[i][j] = -1

        row = [1,0,-1,0]
        col = [0,1,0,-1]

        for r,c in zip(row,col):
            self.dfs(A,i+r,j+c,count - 1)

        A[i][j] = 0

    def Solve(self,A):
        m = len(A)
        n = len(A[0])
        self.count = 0
        count = 1
        self.ans = []
        global x,y
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    count += 1
                if A[i][j] == 1:
                    x = i
                    y = j
        self.dfs(A,x,y,count)
        return self.count,count


if __name__ == '__main__':
    A = [[1,0,0,0],
         [0,0,0,0],
         [0,0,2,-1]]
    B = Solution()
    print(B.Solve(A))
