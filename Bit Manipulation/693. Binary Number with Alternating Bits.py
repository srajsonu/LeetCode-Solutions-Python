class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n).replace('0b', '')
        A = [i for i in n]

        for i in range(1, len(A)):
            if A[i - 1] == A[i]:
                return False

        return True
