from heapq import *
class Solution:
    def solve(self, A):
        if not A: return 0

        m = len(A)
        n = len(A[0])

        heap = []
        visit = set()

        for i in (0, m-1):
            for j in range(n):
                heappush(heap, (A[i][j], i, j))
                visit.add((i, j))

        for j in (0, n-1):
            for i in range(m):
                if (i, j) in visit:
                    continue

                heappush(heap, (A[i][j], i, j))
                visit.add((i, j))

        row = [1, 0, -1, 0]
        col = [0, 1, 0, -1]

        ans = 0
        mx = float('-inf')

        while heap:
            val, i, j = heappop(heap)
            mx = max(mx, val)

            for r,c in zip(row, col):
                nRow = i + r
                nCol = j + c

                if nRow < 0 or nRow >= m or nCol < 0 or nCol >= n or (nRow, nCol) in visit:
                    continue

                if mx > A[nRow][nCol]:
                    ans += mx - A[nRow][nCol]

                heappush(heap, (A[nRow][nCol], nRow, nCol))
                visit.add((nRow, nCol))

        return ans


if __name__ == '__main__':
    A = [[1, 4, 3, 1, 3, 2],
         [3, 2, 1, 3, 2, 4],
         [2, 3, 3, 2, 3, 1]]

    B = Solution()
    print(B.solve(A))
