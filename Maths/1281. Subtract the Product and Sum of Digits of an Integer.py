class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = [i for i in str(n)]
        pdt = 1
        sm = 0
        for i in n:
            pdt *= int(i)
            sm += int(i)

        return pdt - sm
