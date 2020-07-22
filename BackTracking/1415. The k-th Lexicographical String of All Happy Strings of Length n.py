class Solution:
    def generate(self,A,n,k,aux):
        if len(self.ans) == k:
            return

        if len(aux) == n:
            self.ans.append(aux)
            return

        for i in range(3):
            if len(aux) == 0 or aux[-1] != A[i]:
                self.generate(A,n,k,aux + A[i])


    def Solve(self,A,B):
        data = ['a', 'b', 'c']
        self.ans = []
        self.generate(data,A,B,"")
        return self.ans[-1] if len(self.ans) == B else ""

if __name__ == '__main__':
    A = 3
    B = 9
    C = Solution()
    print(C.Solve(A,B))
