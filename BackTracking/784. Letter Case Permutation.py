class Solution:
    def backtrack(self,A,index):
        if index == len(A):
            self.aux.append("".join(A))
            return

        if A[index].isalpha():
            A[index] = A[index].lower()
            self.backtrack(A, index + 1)
            A[index] = A[index].upper()
            self.backtrack(A, index+1)
        else:
            self.backtrack(A,index+1)

    def Solve(self,A):
        A = [i for i in A]
        self.aux = []
        self.backtrack(A,0)
        return self.aux

if __name__ == '__main__':
    A = "a1b2"
    B = Solution()
    print(B.Solve(A))
