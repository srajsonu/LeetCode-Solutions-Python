class Solution:
    def maxProfit(self, A):
        n = len(A)
        peak = A[0]
        valley = A[0]
        i = 0
        ans = 0
        while i < n-1:
            while i < n-1 and A[i] >= A[i+1]:
                i += 1
            valley = A[i]

            while i < n-1 and A[i] <= A[i+1]:
                i += 1

            peak = A[i]
            ans += (peak - valley)

        return ans


if __name__ == '__main__':
    A = [7,1,5,3,6,4]
    B = Solution()
    print(B.maxProfit(A))
