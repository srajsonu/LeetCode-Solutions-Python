class Solution:
    def backtrack(self,A,idx):
        if idx == len(A) and len(self.ans) >= 3:
            return True

        for i in range(idx, len(A)):
            if A[idx] == '0' and i > idx:
                break

            num = int(A[idx:i+1])

            if num > 2**31 - 1:
                break

            size = len(self.ans)

            if size >= 2 and num > self.ans[-1] + self.ans[-2]:
                break

            if size <= 1 or num == self.ans[-1] + self.ans[-2]:
                self.ans.append(num)

                if self.backtrack(A, i+1):
                    return True
                self.ans.pop()
        return False


    def Solve(self,A):
        self.ans = []
        self.backtrack(A,0)
        return self.ans

if __name__ == '__main__':
    A = "123456579"
    B = Solution()
    print(B.Solve(A))
