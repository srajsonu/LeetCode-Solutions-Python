class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        xor = x ^ y
        for _ in range(32):
            cnt += xor & 1
            xor >>= 1
        return cnt
