class Solution:
    def generate(self,A,index,aux):
        if index == len(A):
            print(aux)
            return

        for i in range(len(A)):
            self.generate(A,index+1,aux+A[index])

    def Solve(self,A):
        gray = ['00', '01', '11', '10']
        self.generate(gray,0,'0')

if __name__ == '__main__':
    A = 2
    B = Solution()
    print(B.Solve(A))
