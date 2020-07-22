class Solution:
    def backtrack(self,A,index,vis):
        if index == len(A):
            return

        for i in range(len(A)):
            if vis[i]:
                continue

            if i - 1 >= 0 and A[i] == A[i-1] and not vis[i-1]:
                continue

            self.count += 1
            vis[i] = True
            self.backtrack(A, index+1, vis)
            vis[i] = False

    def Solve(self,A):
        A = [i for i in A]
        A.sort()
        vis = [False for _ in range(len(A))]
        self.count = 0
        self.backtrack(A, 0, vis)
        return self.count

if __name__ == '__main__':
    A = "CDC"
    B = Solution()
    print(B.Solve(A))
