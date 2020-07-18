class Solution:
    def backtrack(self,A,l,r,aux):
        if len(aux) == 2*A:
            self.ans.append(aux)
            return

        if l < A:
            self.backtrack(A, l+1,r,aux+'(')

        if r < l:
            self.backtrack(A, l, r+1,aux+')')

    def Solve(self,A):
        self.ans = []
        self.backtrack(A,0,0,"")
        return self.ans

if __name__ == '__main__':
    A = 3
    B = Solution()
    print(B.Solve(A))
