class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] != 1:
            return False
        return True

    def solve(self, A):
        m = len(A)
        n = len(A[0])
        row = [1, 0, -1, 0]
        col = [0, 1, 0, -1]
        peri = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    cnt = 0
                    for r, c in zip(row, col):
                        nRow = i + r
                        nCol = j + c
                        if self.isValid(A, nRow, nCol):
                            cnt += 1
                    peri += 4 - cnt

        return peri


if __name__ == '__main__':
    A = [[0, 1, 0, 0],
         [1, 1, 1, 0],
         [0, 1, 0, 0],
         [1, 1, 0, 0]]

    B = Solution()
    print(B.solve(A))
