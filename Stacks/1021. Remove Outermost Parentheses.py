class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans = []
        cnt = 0
        for i in S:
            if i == '(' and cnt > 0:
                ans.append(i)
            if i == ')' and cnt > 1:
                ans.append(i)
            cnt += 1 if i == '(' else -1

        return ''.join(ans)
