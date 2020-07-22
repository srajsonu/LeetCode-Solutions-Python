class Solution:
    def isValid(self,s,n1,n2):
        if s == "":
            return True

        n3 = str(n1+n2)
        idx = min(len(s), len(n3))
        if s[:idx] == n3:
            return self.isValid(s[idx:],n2,int(n3))
        return False

    def Solve(self,A):
        n = len(A)
        for i in range(1,n-1):
            n1 =  int(A[:i])
            if str(n1) != A[:i]:
                break
            for j in range(i+1,n):
                n2 = int(A[i:j])
                if str(n2) != A[i:j]:
                    break
                if self.isValid(A[j:],n1,n2): return True
        return False

if __name__ == '__main__':
    A = '112358'
    B = Solution()
    print(B.Solve(A))
