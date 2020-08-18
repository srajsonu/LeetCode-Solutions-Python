from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] == 0:
            return False
        return True

    def dfs(self,A,i,vis):
        for j in range(len(A)):
            if A[i][j] == 1 and not vis[j]:
                vis[j] = True
                self.dfs(A,j, vis)

    def Solve(self, A):
        n = len(A)
        vis = [False for _ in range(n)]
        cnt = 0
        for i in range(n):
            if not vis[i]:
                self.dfs(A, i, vis)
                cnt += 1

        return cnt

    def findCircleNum(self, M):
        m = len(M)
        n = len(M[0])
        q = deque()
        vis = [[False] * n for _ in range(m)]

        row = [1, 0, -1, 0]
        col = [0, 1, 0, -1]
        count = 0
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1 and not vis[i][j]:
                    q.append((i, j))
                    vis[i][j] = True
                    while q:
                        size = len(q)
                        for _ in range(size):
                            s, t = q.popleft()
                            # vis[s][t] = True
                            for r, c in zip(row, col):
                                nRow = s + r
                                nCol = t + c
                                if self.isValid(M, nRow, nCol) and not vis[nRow][nCol]:
                                    vis[nRow][nCol] = True
                                    q.append((nRow, nCol))
                    count += 1
        return count


if __name__ == '__main__':
    A = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]

    C = [[1,0,0,1],
         [0,1,1,0],
         [0,1,1,1],
         [1,0,1,1]]

    B = Solution()
    print(B.findCircleNum(A))
    print(B.Solve(C))
