class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))

if __name__ == '__main__':
    A = '23'
    B = '32'
    C = Solution()
    print(C.addStrings(A, B))
