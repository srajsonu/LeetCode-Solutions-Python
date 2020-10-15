class Solution:
    def backtrack(self, A, index, aux):
        if index == len(A):
            self.ans.append(aux)
            return

        for i in range(index, len(A)):
            A[i], A[index] = A[index], A[i]
            self.backtrack(A, index + 1, aux + [A[index]])
            A[i], A[index] = A[index], A[i]

    def permute(self, nums):
        self.ans = []
        self.backtrack(nums, 0, [])
        return self.ans
