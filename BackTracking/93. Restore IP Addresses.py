class Solution:
    def dfs(self,A,index,aux):
        if index == 4:
            if not A:
                self.ans.append(aux[:-1])
            return

        for i in range(1,4):
           if i <= len(A):
               if int(A[:i]) <= 255:
                    self.dfs(A[i:], index+1, aux + A[:i]+'.')
               if A[0] == '0':
                   break


    def Solve(self,A):
        self.ans = []
        self.dfs(A,0,"")
        return self.ans

if __name__ == '__main__':
    A = "25525511135"
    B = Solution()
    print(B.Solve(A))
