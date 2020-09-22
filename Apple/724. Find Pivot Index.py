class Solution:
    def pivotIndex(self, A):
        sm = sum(A)
        lsm = 0

        for i, j in enumerate(A):
            if lsm == sm - lsm - j:
                return i
            lsm += j

        return -1


if __name__ == '__main__':
    A = [1, 7, 3, 6, 5, 6]
    B = Solution()
    print(B.pivotIndex(A))
