class Solution:
    def backtrack(self,A,index,aux):
        if index == len(A):
            self.ans.append(list(A))
            return

        for i in range(index, len(A)):
            if i > index and A[i] == A[index]:
                continue
            A[i], A[index] = A[index], A[i]
            self.backtrack(list(A), index+1,aux + [A[index]])

    def Solve(self,A):
        A.sort()
        self.ans = []
        self.backtrack(A,0,[])
        return self.ans

if __name__ == '__main__':
    A = [2,3,3]
    B = Solution()
    print(B.Solve(A))
