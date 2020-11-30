class Solution:
    def addDigits(self, num):
        if num == 0: return 0
        if num % 9 == 0: return 9
        return num % 9

if __name__ == '__main__':
    A = 38
    B = Solution()
    print(B.addDigits(A))
