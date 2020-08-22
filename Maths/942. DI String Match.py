from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        n = len(S)

        inc = n
        dec = 0

        ans = []
        for i in range(n):
            if S[i] == 'I':
                ans.append(dec)
                dec += 1
            else:
                ans.append(inc)
                inc -= 1

        if S[-1] == 'I':
            ans.append(dec)
        else:
            ans.append(inc)

        return ans

