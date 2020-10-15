class Solution:
    def maxProfit(self, A) -> int:
        n = len(A)
        mx_profit = 0
        min_price = float('inf')

        for i in range(n):
            if A[i] < min_price:
                min_price = A[i]

            elif A[i] - min_price > mx_profit:
                mx_profit = A[i] - min_price

        return mx_profit
