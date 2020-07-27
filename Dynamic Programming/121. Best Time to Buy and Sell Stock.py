class Solution:
    def Solve(self,A):
        n = len(A)
        max_profit = 0
        min_price = float('inf')
        for i in range(n):
            if min_price > A[i]:
                min_price = A[i]
            elif max_profit < A[i] - min_price:
                max_profit = A[i] - min_price

        return max_profit

if __name__ == '__main__':
    A = [7,1,5,3,6,4]
    B = Solution()
    print(B.Solve(A))
