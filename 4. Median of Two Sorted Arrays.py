class Solution:
    def findMedian(self, A, B, m, n):
        if m > n:
            return self.findMedian(B, A, n, m)

        l = 0
        h = m

        while l <= h:
            midA = (l + h) // 2
            midB = (m + n + 1) // 2 - midA

            maxLeftA = float('-inf') if midA == 0 else A[midA - 1]
            minRightA = float('inf') if midA == m else A[midA]

            maxLeftB = float('-inf') if midB == 0 else B[midB - 1]
            minRightB = float('inf') if midB == n else B[midB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 != 0:
                    return max(maxLeftA, maxLeftB)
                else:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2

            elif maxLeftA > minRightB:
                h = midA - 1
            else:
                l = midA + 1

    def solve(self, A, B):
        m = len(A)
        n = len(B)
        return self.findMedian(A, B, m, n)


if __name__ == '__main__':
    A = []
    B = [3]
    C = Solution()
    print(C.solve(A, B))
