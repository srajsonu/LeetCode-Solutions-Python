class Solution:
    def isPalindrome(self,A):
        return A == A[::-1]

    def partition(self,A,index,aux):
        if index == len(A):
            return

        for i in range(index, len(A)):
            if self.isPalindrome(A[index:i+1]):
                self.count += 1
                self.partition(A,index+1,aux)

    def Solve(self,A):
        self.count = 0
        self.partition(A,0,[])
        return self.count

if __name__ == '__main__':
    A = 'aab'
    B = Solution()
    print(B.Solve(A))
