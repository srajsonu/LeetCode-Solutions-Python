class Solution:
    def merge(self, A):
        n = len(A)
        A.sort(key= lambda i: i[0])
        stack = []
        stack.append(A[0])
        for i in range(1, n):
            tmp = A[i]

            if tmp[0] <= stack[-1][1] and tmp[1] > stack[-1][1]:
                stack[-1][1] = tmp[1]

            if tmp[0] > stack[-1][1]:
                stack.append(tmp)

        return stack


if __name__ == '__main__':
    A = [[1, 3], [2, 6], [8, 10], [15, 18]]
    B = Solution()
    print(B.merge(A))
