from math import log

class Solution:
    def solve(self, num):
        if num <= 0: return False
        m = log(num, 4)
        return int(m) == m

if __name__ == '__main__':
    A = 16
    B = Solution()
    print(B.solve(A))
