class Solution:
    def solve(self, A):
        A.sort(key=lambda i: i[0])
        n = len(A)
        ans = [A[0]]

        for i in range(1, n):
            if A[i][0] <= ans[-1][1]:
                ans[-1][1] = max(A[i][1], ans[-1][1])
            else:
                ans.append(A[i])

        return ans


if __name__ == '__main__':
    A = [[1, 3],
         [2, 6],
         [8, 10],
         [15, 18]]

    B = Solution()
    print(B.solve(A))
