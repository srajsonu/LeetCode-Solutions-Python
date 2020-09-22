class Solution:
    def sumOddLengthSubarrays(self, A):  # Brute-force: O(n^3) got accepted
        n = len(A)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                arr = A[i:j]
                if len(arr) % 2 != 0:
                    ans += sum(arr)
        return ans

    def solve(self, A):
        ans, curr = 0, 0
        sm = [0, 0]

        for i, j in enumerate(A):
            curr += j
            sm[i % 2] += curr
            ans += curr * (i // 2 + 1) - sm[1 - i % 2]

        return ans


if __name__ == '__main__':
    A = [1, 4, 2, 5, 3]
    B = Solution()
    print(B.solve(A))
