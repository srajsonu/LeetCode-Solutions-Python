class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in reversed(range(32)):
            #n & 1 get the right-most bit
            ans += (n & 1) << i
            n >>= 1
        return ans
