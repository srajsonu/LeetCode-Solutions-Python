class Solution:
    def isUnique(self,A):
        aux = set()
        for i in A:
            if i in aux:
                return False
            aux.add(i)
        return True

    def backtrack(self,A,index,aux):
        if self.isUnique(aux):
            self.ans = max(self.ans, len(aux))

        if index == len(A) or not self.isUnique(aux):
            return

        for i in range(index, len(A)):
            self.backtrack(A,i+1,aux+A[i])

    def Solve(self,A):
        self.ans = float('-inf')
        self.backtrack(A, 0,"")
        return self.ans

if __name__ == '__main__':
    A = ["un","iq","ue"]
    B = Solution()
    print(B.Solve(A))
