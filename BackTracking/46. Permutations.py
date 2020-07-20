class Solution:
    def permute(self,A,indx,aux):
        if indx == len(A):
            print(aux)
            return

        for i in range(indx, len(A)):
            A[i], A[indx] = A[indx], A[i]
            self.permute(A,indx+1,aux+[A[indx]])
            A[i], A[indx] = A[indx], A[i]

    def Solve(self,A):
        return self.permute(A,0,[])

if __name__ == '__main__':
    A = [1,2,3]
    B = Solution()
    print(B.Solve(A))
