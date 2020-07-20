class Solution:
    def combinations(self,A,B,C,index,aux):
        if index == 9:
            if sum(aux) == B and len(aux) == C:
                self.ans.append(aux)
            return

        pick = self.combinations(A,B,C,index+1,aux + [A[index]])
        dont = self.combinations(A,B,C,index+1,aux)
        return pick and dont

    def Solve(self, A, B):
        self.ans = []
        data = [i for i in range(1,10)]
        self.combinations(data,B,A,0,[])
        return self.ans

if __name__ == '__main__':
    A = 2
    B = 18
    C = Solution()
    print(C.Solve(A,B))
