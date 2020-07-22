class Solution:
    def backtrack(self,n, index, vis):
        if index > n:
            self.count += 1

        for i in range(1,n+1):
            if not vis[i] and (index % i == 0 or i % index == 0):
                vis[i] = True
                self.backtrack(n,index+1,vis)
                vis[i] = False


    def Solve(self,A):
        self.count = 0
        vis = [False for _ in range(A+1)]
        self.backtrack(A,1,vis)
        return self.count

if __name__ == '__main__':
    A = 6
    B = Solution()
    print(B.Solve(A))
