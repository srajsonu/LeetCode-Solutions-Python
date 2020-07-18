class Solution:
    def backtrack(self,A,B,i,aux):
        if sum(aux) > B:
            return 0

        if i == len(A):
            if sum(aux) == B:
                self.ans.append(aux)
            return
        
        take = self.backtrack(A,B, i,aux + [A[i]])
        dont = self.backtrack(A,B, i+1, aux)
        return take and dont

    def Solve(self,A,B):
        self.ans = []
        self.backtrack(A,B,0,[])
        return self.ans

if __name__ == '__main__':
    A = [2,3,6,7]
    B = 7
    C =Solution()
    print(C.Solve(A,B))
