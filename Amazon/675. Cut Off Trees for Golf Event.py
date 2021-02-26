from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] == 0:
            return False
        return True

    def cutOffTree(self, A):
        m = len(A)
        n = len(A[0])

        print(A)

        row = [-1, 0, 1, 0]
        col = [0, -1, 0, 1]

        q = deque()
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    q.append((i, j, 0))

        if not q:
            A[0][0] = 1
            q.append((0, 0, 1))

        vis = set()
        k = 0
        while q:
            i, j, k = q.popleft()
            vis.add((i, j))
            for r, c in zip(row, col):
                nRow = i + r
                nCol = j + c

                if self.isValid(A, nRow, nCol) and (nRow, nCol) not in vis and A[i][j] < A[nRow][nCol]:
                    A[nRow][nCol] = 1
                    vis.add((nRow, nCol))
                    q.append((nRow, nCol, k + 1))

        for i in range(m):
            for j in range(n):
                if A[i][j] > 1:
                    return -1

        return k


if __name__ == '__main__':
    A = [[54581641, 64080174, 24346381, 69107959],
         [86374198, 61363882, 68783324, 79706116],
         [668150, 92178815, 89819108, 94701471],
         [83920491, 22724204, 46281641, 47531096],
         [89078499, 18904913, 25462145, 60813308]]

    B = Solution()
    print(B.cutOffTree(A))
