class Solution:
    def dp(self, s, dic):
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in dic:
                    dp[i] = True
                    break

        return dp[-1]

    def backtrack(self, s, dic, aux):
        if self.dp(s, dic):
            if not s:
                self.ans.append(aux[:-1])
                return

            for i in range(1, len(s) + 1):
                if s[:i] in dic:
                    self.backtrack(s[i:], dic, aux + s[:i] + " ")

    def wordBreak(self, s, dic):
        dic = set(dic)
        self.ans = []
        self.backtrack(s, dic, "")
        return self.ans
