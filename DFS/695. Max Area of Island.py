from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] == 0:
            return False
        return True

    def dfs(self, A, i, j, vis):
        if not self.isValid(A, i, j):
            return 0

        vis[i][j] = True
        row = [0, 1, 0, -1]
        col = [1, 0, -1, 0]
        ans = A[i][j]
        for r, c in zip(row, col):
            nRow = i + r
            nCol = j + c
            if self.isValid(A, nRow, nCol) and not vis[nRow][nCol]:
                ans += self.dfs(A, nRow, nCol, vis)

        return ans

    def Solve(self, A):
        m = len(A)
        n = len(A[0])
        ans = float('-inf')
        vis = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and not vis[i][j]:
                    a = self.dfs(A, i, j, vis)
                    ans = max(ans, a)

        return ans


    def maxAreaOfIsland(self, A):
        m = len(A)
        n = len(A[0])
        vis = [[False] * n for _ in range(m)]

        row = [0, 1, 0, -1]
        col = [1, 0, -1, 0]
        q = deque()
        ans = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and not vis[i][j]:
                    count = 0
                    q.append((i, j))
                    while q:
                        s, t = q.popleft()
                        count += 1
                        vis[s][t] = True
                        for r, c in zip(row, col):
                            nRow = s + r
                            nCol = t + c

                            if self.isValid(A, nRow, nCol) and not vis[nRow][nCol]:
                                vis[nRow][nCol] = True
                                q.append((nRow, nCol))
                    ans = max(ans, count)
        return ans


if __name__ == '__main__':
    A = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    C = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

    B = Solution()
    print(B.maxAreaOfIsland(C))
    print(B.Solve(C))
