class Solution:
    def countPrimes(self, n):
        cnt = 0
        prime = [True for _ in range(n)]

        for i in range(2, n):
            if not prime[i]:
                continue

            cnt += 1
            j = i*i
            while j < n:
                prime[j] = False
                j += i

        return cnt

if __name__ == '__main__':
    n = 10
    s = Solution()
    print(s.countPrimes(n))
