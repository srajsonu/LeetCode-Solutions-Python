class Solution:
    def subsets(self,A,index,aux,p):
        if p:
            if aux not in self.ans:
                self.ans.append(aux)
                
        if index == len(A):
            return

        pick = self.subsets(A,index+1, aux + [A[index]],True)
        dont = self.subsets(A,index+1,aux,False)
        return pick and dont

    def Solve(self,A):
        A.sort()
        self.ans = []
        self.subsets(A,0,[],True)
        return self.ans


if __name__ == '__main__':
    A = [1,2,2]
    B = Solution()
    print(B.Solve(A))
