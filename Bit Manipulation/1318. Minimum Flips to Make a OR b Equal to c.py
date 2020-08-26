class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        equal = (a | b) ^ c
        for i in range(32):
            mask = 1 << i
            if  equal & mask:
                cnt += 2 if (a & mask) == (b & mask) and (c & mask) == 0 else 1
        return cnt
