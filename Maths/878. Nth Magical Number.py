class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)

    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        mod = 10 ** 9 + 7
        lcm = self.lcm(A, B)
        low = 2
        high = 10 ** 17

        while low < high:
            mid = (low + high) // 2
            target = mid // A + mid // B - mid // lcm

            if target < N:
                low = mid + 1
            else:
                high = mid

        return high % mod
