class Solution:
    def isValid(self, col_placements):
        rowId = len(col_placements) - 1
        for i in range(rowId):
            diff = abs(col_placements[i] - col_placements[rowId])
            if diff == 0 or diff == rowId - i:
                return False

        return True

    def solveNQueens(self, n, row, col_placements):
        if row == n:
            print(col_placements)
            self.ans.append(list(col_placements))
            return

        for col in range(n):
            col_placements.append(col)
            if self.isValid(col_placements):
                self.solveNQueens(n,row+1,col_placements)
            col_placements.pop()


    def Solve(self,A):
        self.ans = []
        self.solveNQueens(A,0,[])
        result = []
        for i in self.ans:
            tmp1 = []
            for j in range(len(i)):
                tmp = ['.' for _ in range(len(i))]
                tmp[i[j]] = 'Q'
                tmp1.append("".join(tmp))
            result.append(tmp1)
        return result

if __name__ == '__main__':
    A = 4
    B = Solution()
    print(B.Solve(A))
