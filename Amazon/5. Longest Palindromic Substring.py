class Solution:
    def isPalindrome(self, A, i, j):
        while i >= 0 and j < len(A) and A[i] == A[j]:
            i -= 1
            j += 1

        if self.mx < j - i - 1:
            self.mx = j - i - 1
            self.start = i + 1


    def longestPalindrome(self, A):
        self.mx = 1
        self.start = 0
        n = len(A)

        if n < 2:
            return A

        for i in range(n):
            self.isPalindrome(A, i, i)
            self.isPalindrome(A, i, i+1)

        return A[self.start:self.start+self.mx]


if __name__ == '__main__':
    A = "aacabakaca"
    B = Solution()
    print(B.longestPalindrome(A))
