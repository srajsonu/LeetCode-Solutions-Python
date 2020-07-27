class Solution:
    def dp(self, A, aux, ans):
        if A == []:
            print(aux, )
            for i in aux:
                if i not in ans:
                    ans.append(i)
            return

        for i in range(1, len(A) + 1):
            # print(sum(A[:i]),A[:i])
            # if sum(A[:i]) % 2 != 0:
            self.dp(A[i:], aux + [A[:i]], ans)

    def Solve(self, A):
        ans = []
        self.dp(A, [], ans)
        self.ans = []
        return len(ans), ans


if __name__ == '__main__':
    A = [100, 100, 99, 99]
    B = Solution()
    print(B.Solve(A))
