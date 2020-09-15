class Solution:
    def threeSum(self, A):
        A.sort()
        n = len(A)
        ans = []

        for i in range(n):
            if i > 0 and A[i - 1] == A[i]:
                continue

            target = A[i] * -1
            s = i + 1
            e = n - 1

            while s < e:
                if A[s] + A[e] == target:
                    ans.append([A[i], A[s], A[e]])
                    s += 1
                    while s < e and A[s] == A[s - 1]:
                        s += 1
                elif A[s] + A[e] < target:
                    s += 1
                else:
                    e -= 1

        return ans
