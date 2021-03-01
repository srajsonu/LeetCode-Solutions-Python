class Solution:
    def maxProfit(self, A):
        n = len(A)
        min_cost = float('inf')
        ans = 0
        for i in range(n):
            min_cost = min(min_cost, A[i])
            ans = max(A[i] - min_cost, ans)

        return ans

if __name__ == '__main__':
    A = [7, 1, 5, 3, 6, 4]
    B = Solution()
    print(B.maxProfit(A))
