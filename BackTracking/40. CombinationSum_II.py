from collections import Counter
class Solution:
    def dfs(self,A,B,index,aux):
        if B < 0:
            return

        if B == 0:
            self.ans.append(aux)
            return

        for i in range(index, len(A)):
            if i > index and A[i] == A[i-1]:
                continue

            if A[i] > B:
                break

            self.dfs(A,B-A[i],i+1,aux+[A[i]])

    def Solve(self,A, B):
        self.ans = []
        self.count = Counter(A)
        A.sort()
        self.dfs(A,B,0,[])
        return self.ans

if __name__ == '__main__':
    A = [10,1,2,7,6,1,5]
    B = 8
    C = Solution()
    print(C.Solve(A, B))
