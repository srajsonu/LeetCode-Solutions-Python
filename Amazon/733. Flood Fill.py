from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        return True

    def floodFill(self, A, B, C, D):
        q = deque()
        q.append((B, C, A[B][C]))
        vis = set()
        row = [-1, 0, 1, 0]
        col = [0, -1, 0, 1]

        while q:
            i, j, k = q.popleft()
            A[i][j] = D
            vis.add((i, j))
            for r, c in zip(row, col):
                nRow = i + r
                nCol = j + c
                if self.isValid(A, nRow, nCol) and (nRow, nCol) not in vis and A[nRow][nCol] == k:
                    A[nRow][nCol] = D
                    vis.add((nRow, nCol))
                    q.append((nRow, nCol, k))

        return A


if __name__ == '__main__':
    A = [[0, 0, 0], [0, 0, 0]]
    B = 0
    C = 0
    D = 2
    E = Solution()
    print(E.floodFill(A, B, C, D))
