class Solution:
    def maxProfit(self, A):
        n = len(A)
        peak = A[0]
        valley = A[0]
        i = 0
        ans = []
        while i < n-1:
            while i < n-1 and A[i] >= A[i+1]:
                i += 1
            valley = A[i]

            while i < n-1 and A[i] <= A[i+1]:
                i += 1
            peak = A[i]

            ans.append(peak-valley)
            
        if len(ans) == 1:
            return ans[0]

        res = 0
        for i in range(len(ans)):
            for j in range(i+1, len(ans)):
                res = max(res, ans[i] + ans[j])

        return res

if __name__ == '__main__':
    A = [1,2,4,2,5,7,2,4,9,0]
    B = Solution()
    print(B.maxProfit(A))
