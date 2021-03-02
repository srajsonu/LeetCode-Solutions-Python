class Solution:
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)

        if m > n:
            return self.findMedianSortedArrays(B, A)

        l = 0
        h = m

        while l <= h:
            midA = (l + h) // 2
            midB = (m + n + 1) // 2 - midA

            maxLeftA = float('-inf') if midA == 0 else A[midA-1]
            minRightA = float('inf') if midA == m else A[midA]

            maxLeftB = float('-inf') if midB == 0 else B[midB-1]
            minRightB = float('inf') if midB == n else B[midB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 != 0:
                    return max(maxLeftA, maxLeftB)
                else:
                    return  (max(maxLeftA, maxLeftB) + min(minRightA,  minRightB)) / 2
            elif maxLeftA > minRightB:
                h = midA - 1
            else:
                l = midA + 1

        return -1


if __name__ == '__main__':
    A = [1, 3, 8, 9, 15]
    B = [7, 11, 18, 19, 21, 25]
    C = Solution()
    print(C.findMedianSortedArrays(A, B))
