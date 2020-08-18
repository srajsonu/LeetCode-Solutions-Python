from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        return True

    def dfs(self, A, i, j, q, vis, ):
        vis[i][j] = True
        q.append((i, j))
        row = [0, 1, 0, -1]
        col = [1, 0, -1, 0]

        for r, c in zip(row, col):
            nRow = i + r
            nCol = j + c
            if self.isValid(A, nRow, nCol) and not vis[nRow][nCol] and A[nRow][nCol] == 1:
                vis[nRow][nCol] = True
                self.dfs(A, nRow, nCol, q, vis)

    def Solve(self, A):
        m = len(A)
        n = len(A[0])
        q = deque()
        found = False
        vis = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    self.dfs(A, i, j, q, vis)
                    found = True
                    break
            if found:
                break

        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                row = [1, 0, -1, 0]
                col = [0, 1, 0, -1]
                for r, c in zip(row, col):
                    nRow = i + r
                    nCol = j + c
                    if self.isValid(A, nRow, nCol) and not vis[nRow][nCol]:
                        if A[nRow][nCol] == 1:
                            return level
                        q.append((nRow, nCol))
                        vis[nRow][nCol] = True
            level += 1

        return -1


if __name__ == '__main__':
    A = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    B = Solution()
    print(B.Solve(A))
