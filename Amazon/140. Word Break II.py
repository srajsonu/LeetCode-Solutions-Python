class Solution:
    def dp(self, A, B):
        n = len(A)
        B = set(B)

        dp = [False for _ in range(n + 1)]
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and A[j:i] in B:
                    dp[i] = True
                    break

        return dp[-1]

    def backtrack(self, A, B, aux):
        if self.dp(A, B):
            if not A:
                self.ans.append(aux[:-1])
                return

            for i in range(1, len(A)+1):
                if A[:i] in B:
                    self.backtrack(A[i:], B, aux + A[:i] + " ")

    def wordBreak(self, A, B):
        self.ans = []
        self.backtrack(A, B, "")
        return self.ans


if __name__ == '__main__':
    A = "catsanddog"
    B = ["cat", "cats", "and", "sand", "dog"]
    C = Solution()
    print(C.wordBreak(A, B))
