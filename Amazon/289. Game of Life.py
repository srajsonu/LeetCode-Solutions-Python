from collections import deque


class Solution:
    def isvalid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[i]):
            return False
        return True

    def solve(self, A):
        m = len(A)
        n = len(A[0])

        row = [-1, 0, 1, 0, -1, -1, 1, 1]
        col = [0, -1, 0, 1, -1, 1, -1, 1]

        q = deque()

        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    q.append((i, j))
        vis = set()
        while q:
            i, j = q.popleft()
            vis.add((i, j))
            for r, c in zip(row, col):
                nRow = i + r
                nCol = j + c

                if self.isvalid(A, nRow, nCol) and (nRow, nCol) not in vis:
                    vis.add((nRow, nCol))

if __name__ == '__main__':
    A = [[0, 1, 0],
         [0, 0, 1],
         [1, 1, 1],
         [0, 0, 0]]
    B = Solution()
    print(B.solve(A))
