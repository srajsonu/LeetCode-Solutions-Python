class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        bal = 0
        cnt = 0
        for c in S:
            if c == '(':
                bal += 1
            else:
                bal -= 1

            if bal == -1:
                cnt += 1
                bal += 1

        return cnt + bal
