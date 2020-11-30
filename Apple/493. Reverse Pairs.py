class Solution:
    def mergeSort(self, A, s, e):
        if s >= e:
            return 0

        mid = (s + e) // 2
        cnt, j = self.mergeSort(A, s, mid) + self.mergeSort(A, mid+1, e), mid + 1

        for i in range(s, mid+1):
            while j <= e and A[i] > 2 * A[j]:
                j += 1
            cnt += j - (mid + 1)

        A[s:e+1] = sorted(A[s:e+1])
        return cnt

    def reversePairs(self, arr):
        n = len(arr)
        return self.mergeSort(arr, 0, n-1)


if __name__ == '__main__':
    A = [1,3,2,3,1]
    B = Solution()
    print(B.reversePairs(A))
