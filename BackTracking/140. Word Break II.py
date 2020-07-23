class Solution:
    def check(self,s,dic):
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in dic:
                    dp[i] = True
        return dp[-1]

    def backtrack(self,s,dic,aux):
        if self.check(s,dic):
            if not s:
                self.ans.append(aux[:-1])
                return
            for i in range(1,len(s)+1):
                if s[:i] in dic:
                    self.backtrack(s[i:],dic,aux + s[:i] + " ")

    def wordBreak(self,A,B):
        self.ans = []
        self.backtrack(A,B,"")
        return self.ans

if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    C = Solution()
    print(C.wordBreak(s,wordDict))
