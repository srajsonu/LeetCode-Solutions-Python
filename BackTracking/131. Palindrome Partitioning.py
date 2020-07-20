class Solution:
    def isPalindrome(self,A):
        return A == A[::-1]

    def dfs(self,A,index,aux):
        if index == len(A):
            self.ans.append(aux)
            return

        for i in range(index, len(A)):
            if self.isPalindrome(A[index:i+1]):
                self.dfs(A,i+1,aux + [A[index:i+1]])

    def Solve(self,A):
        self.ans = []
        self.dfs(A,0,[])
        return self.ans

if __name__ == '__main__':
    A = 'aab'
    B = Solution()
    print(B.Solve(A))
