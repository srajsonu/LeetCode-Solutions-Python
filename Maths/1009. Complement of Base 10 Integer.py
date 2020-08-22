class Solution:
    def bitwiseComplement(self, N: int) -> int:
        A = bin(N).replace('0b', '')
        A = [i for i in A]
        for i in range(len(A)):
            if A[i] == '1':
                A[i] = '-1'

            if A[i] == '0':
                A[i] = '1'

        for i in range(len(A)):
            if A[i] == '-1':
                A[i] = '0'

        return int(''.join(A), 2)
