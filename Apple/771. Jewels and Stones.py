class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freq = {}

        for i in S:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        cnt = 0
        for i in J:
            if i in freq:
                cnt += freq[i]

        return cnt
