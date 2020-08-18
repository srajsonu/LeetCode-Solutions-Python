from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        return True

    def Solve(self, A):
        if A[0][0] == 1 or A[-1][-1] == 1: return -1
        m = len(A)
        n = len(A[0])
        q = deque()
        t = 1
        q.append((0,0,t))
        while q:
            i,j, t = q.popleft()
            A[i][j] = 1
            row = [-1, 0, 1, 0, -1, 1, -1, 1]
            col = [0, -1, 0, 1, -1, 1, 1, -1]

            for r, c in zip(row, col):
                nRow = i + r
                ncol = j + c

                if self.isValid(A,nRow,ncol) and A[nRow][ncol] == 0:
                    A[nRow][ncol] = 1
                    q.append((nRow, ncol, t+1))

            if i == m-1 and j == n-1:
                return t

        return -1

if __name__ == '__main__':
    A = [[0,0,0],[1,1,0],[1,1,0]]
    B = Solution()
    print(B.Solve(A))
