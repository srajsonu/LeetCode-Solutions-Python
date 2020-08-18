from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        return True

    def dfs(self, A, i, j):
        if A[i][j] != 'E':
            return

        row = [-1, 0, 1, 0, -1, 1, -1, 1]
        col = [0, -1, 0, 1, -1, 1, 1, -1]

        mineCount = 0
        for r, c in zip(row, col):
            nRow = i + r
            nCol = j + c

            if self.isValid(A, nRow, nCol) and A[nRow][nCol] == 'M':
                mineCount += 1

        if mineCount == 0:
            A[i][j] = 'B'
        else:
            A[i][j] = str(mineCount)
            return

        for r, c in zip(row, col):
            nRow = i + r
            nCol = j + c
            if self.isValid(A, nRow, nCol):
                self.dfs(A, nRow, nCol)

    def solve(self, A, B):
        if not A:
            return []

        if A[B[0]][B[1]] == 'M':
            A[B[0]][B[1]] = 'X'
            return A

        self.dfs(A, B[0], B[1])
        return A




if __name__ == '__main__':
    A = [['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'M', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E']]

    B = [3, 0]
    C = Solution()
    print(C.solve(A, B))
