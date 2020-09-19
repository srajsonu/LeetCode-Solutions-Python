class Solution:
    def solve(self, A):
        n = len(A)
        mx_area = 0
        l = 0
        h = n - 1

        while l < h:
            mx_area = max(mx_area, min(A[l], A[h]) * (h - l))
            if A[l] < A[h]:
                l += 1
            else:
                h -= 1

        return mx_area

if __name__ == '__main__':
    A = [1,8,6,2,5,4,8,3,7]
    B = Solution()
    print(B.solve(A))
