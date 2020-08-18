class Solution:
    def permute(self,A,indx,aux):
        if indx == len(A):
            self.aux.append(aux)
            return aux

        for i in range(indx, len(A)):
            A[i], A[indx] = A[indx], A[i]
            self.permute(A,indx+1,aux+[A[indx]])
            A[i], A[indx] = A[indx], A[i]

    def Solve(self,A):
        self.aux = []
        self.permute(A,0,[])
        return self.aux

if __name__ == '__main__':
    A = [2,3,3]
    B = Solution()
    print(B.Solve(A))
