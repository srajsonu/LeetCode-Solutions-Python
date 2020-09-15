class Solution:
    def nSum(self, A, target, N, aux):
        n = len(A)
        if n < N or N < 2 or target < A[0] * N or target > A[-1] * N:
            return

        if N == 2:
            l = 0
            r = n - 1

            while l < r:
                s = A[l] + A[r]
                if s == target:
                    self.ans.append(aux + [A[l], A[r]])
                    l += 1
                    while l < r and A[l] == A[l - 1]:
                        l += 1

                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(n - N + 1):
                if i > 0 and A[i] == A[i - 1]: continue
                self.nSum(A[i + 1:], target - A[i], N - 1, aux + [A[i]])

    def fourSum(self, nums, target):
        self.ans = []
        self.nSum(sorted(nums), target, 4, [])
        return self.ans

if __name__ == '__main__':
    A = []
    C = 3
    B = Solution()
    print(B.fourSum(A, C))
