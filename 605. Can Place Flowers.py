class Solution:
    def canPlaceFlowers(self, A, n):
        m = len(A)
        ans = 0

        for i in range(m):
            if A[i] == 0 and (i == 0 or A[i - 1] == 0) and (i == m - 1 or A[i + 1] == 0):
                ans += 1
                A[i] = 1

        return ans >= n

if __name__ == '__main__':
    A = [1, 0, 0, 0, 1]
    B = 1
    C = Solution()
    print(C.canPlaceFlowers(A, B))
