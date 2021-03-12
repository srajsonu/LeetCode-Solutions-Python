class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[i]) or A[i][j] == 0:
            return False
        return True

    def dfs(self, A, i, j, vis):
        if not self.isValid(A, i, j):
            return 0

        vis.add((i, j))
        ans = A[i][j]
        row = [-1, 0, 1, 0]
        col = [0, -1, 0, 1]

        for r, c in zip(row, col):
            nRow = i + r
            nCol = j + c

            if self.isValid(A, nRow, nCol) and (nRow, nCol) not in vis:
                vis.add((nRow, nCol))
                ans += self.dfs(A, nRow, nCol, vis)

        return ans

    def maxAreaOfIsland(self, A):
        m = len(A)
        n = len(A[0])
        vis = set()
        ans = float('-inf')

        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and (i, j) not in vis:
                    ans = max(ans, self.dfs(A, i, j, vis))

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
    B = Solution()
    print(B.maxAreaOfIsland(A))
