class Solution:
    def combinations(self,A,B,index,aux):
        if index == len(A):
            if len(aux) == B:
                self.ans.append(aux)
            return

        pick = self.combinations(A,B,index+1, aux + [A[index]])
        dont = self.combinations(A,B,index+1,aux)
        return pick and dont

    def Solve(self,A,B):
        self.ans = []
        data = [i for i in range(1,A+1)]
        self.combinations(data,B,0,[])
        return self.ans

if __name__ == '__main__':
    A = 4
    B = 2
    C = Solution()
    print(C.Solve(A,B))
