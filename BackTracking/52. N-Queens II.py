class Solution:
    def isValid(self, colPlaced):
        rowId = len(colPlaced) - 1
        for i in range(rowId):
            diff = abs(colPlaced[i] - colPlaced[rowId])
            if diff == 0 or diff == rowId - i:
                return False

        return True

    def placeQueens(self, n, row, colPlaced):
        if row == n:
            self.ans.append(list(colPlaced))
            return

        for col in range(n):
            colPlaced.append(col)
            if self.isValid(colPlaced):
                self.placeQueens(n, row + 1, colPlaced)

            colPlaced.pop()

    def totalNQueens(self, n: int) -> int:
        self.ans = []
        self.placeQueens(n, 0, [])
        return len(self.ans)

if __name__ == '__main__':
    A = 4
    B = Solution()
    print(B.totalNQueens(A))
