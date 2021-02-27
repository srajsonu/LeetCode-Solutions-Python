from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] == 0:
            return False
        return True

    def bfs(self, A, sr, sc, tr, tc):
        q = deque()
        q.append((sr, sc, 0))

        row = [-1, 0, 1, 0]
        col = [0, -1, 0, 1]
        vis = set()

        while q:
            i, j, k = q.popleft()
            vis.add((i, j))
            if i == tr and j == tc:
                return k

            for r, c in zip(row, col):
                nRow = i + r
                nCol = j + c

                if self.isValid(A, nRow, nCol) and (nRow, nCol) not in vis:
                    vis.add((nRow, nCol))
                    q.append((nRow, nCol, k+1))
        return -1


    def cutOffTree(self, A):
        m = len(A)
        n = len(A[0])
        trees = []
        sr = 0
        sc = 0

        for i in range(m):
            for j in range(n):
                if A[i][j] > 1:
                    trees.append((A[i][j],i, j))

        trees.sort()
        total_cost = 0
        for h, tr, tc in trees:
            d = self.bfs(A, sr, sc, tr, tc)
            if d < 0:
                return -1

            total_cost += d
            sr = tr
            sc = tc

        return total_cost


if __name__ == '__main__':
    A = [[54581641, 64080174, 24346381, 69107959],
         [86374198, 61363882, 68783324, 79706116],
         [668150, 92178815, 89819108, 94701471],
         [83920491, 22724204, 46281641, 47531096],
         [89078499, 18904913, 25462145, 60813308]]

    B = Solution()
    print(B.cutOffTree(A))
