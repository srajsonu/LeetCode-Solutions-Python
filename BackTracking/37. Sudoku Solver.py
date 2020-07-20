class Solution:
    def checkRow(self,row, val):
        for col in range(9):
            if self.board[row][col] == val:
                return False

        return True

    def checkCol(self,col, val):
        for row in range(9):
            if self.board[row][col] == val:
                return False

        return True

    def checkSquare(self,row,col,val):
        for r in range(row,row+3):
            for c in range(col, col+3):
                if self.board[r][c] == val:
                    return False
        return True

    def isValid(self, row, col , val):
        boxRow = row - row%3
        boxCol = col - col%3
        if self.checkRow(row, val) and\
                self.checkCol(col, val) and\
                self.checkSquare(boxRow, boxCol, val):
            return True
        return False

    def find_unassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row,col
        return -1,-1

    def Solve(self):
        row, col = self.find_unassigned()
        if row == -1 and col == -1:
            return True

        num = [str(i) for i in range(1,10)]
        for val in num:
            if self.isValid(row,col,val):
                self.board[row][col] = val
                if self.Solve():
                    return True
                self.board[row][col] = '.'
        return False

    def solveSudoku(self,A):
        self.board = A
        self.Solve()
        return self.board

if __name__ == '__main__':
    A = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
         ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
         ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
         ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
         ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
         ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
         ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
         ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
         ['.', '.', '.', '.', '8', '.', '.', '7', '9']]

    B = Solution()
    print(B.solveSudoku(A))
