class Solution:
    def check(self, A, B, index):
        m = len(A)
        n = len(B)

        for i in range(m):
            if A[i] != B[(i + index) % n]:
                return False

        return True

    def rotateString(self, A: str, B: str) -> bool:
        m = len(A)
        n = len(B)

        if m != n: return False
        if not A and not B: return True
        if not A or not B: return False

        for i in range(m):
            if self.check(A, B, i):
                return True

        return False

if __name__ == '__main__':
    A = 'kifcqeiqoh'
    B = 'ayyrddojpq'
    C = Solution()
    print(C.rotateString(A, B))
