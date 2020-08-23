class Solution:
    def countPrimes(self, n: int) -> int:
        cnt = 0
        Prime = [True for _ in range(n)]
        for i in range(2, n):
            if not Prime[i]:
                continue
            cnt += 1
            j = i * i
            while j < n:
                Prime[j] = False
                j += i

        return cnt
