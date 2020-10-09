class Solution:
    def intersection(self, A, B):
        A = list(set(A))
        B = set(B)

        m = len(A)
        n = len(B)

        if m < n:
            return self.intersection(B, A)

        ans = []
        for i in range(m):
            if A[i] in B:
                ans.append(A[i])

        return ans
