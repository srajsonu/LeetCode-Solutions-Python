class Solution:
    def isPalindrome(self, A, i, j):
        return A[i:j+1] == A[i:j+1][::-1]

    def dp(self, A, i, j, dp):
        if i > j:
            return 0

        if (i, j) in dp:
            return dp[(i, j)]

        if i == j:
            return 1

        if A[i] == A[j]:
            ans = j - i + 1 + self.dp(A, i+1, j-1, dp)
        else:
            ans = max(self.dp(A, i+1, j, dp), self.dp(A, i, j-1, dp))

        dp[(i, j)] = ans
        return ans

    def longestPalindrome(self, A):
        self.mx = 1
        self.start = 0
        n = len(A)
        dp = {}
        self.dp(A, 0, n-1, dp)
        return A[self.start:self.start+self.mx]


if __name__ == '__main__':
    A = "aacabdkacaa"
    B = Solution()
    print(B.longestPalindrome(A))
