class Solution:
    def shuffle(self, A, n):
        i = 0
        j = n

        ans = []
        while i < n:
            ans.append(A[i])
            ans.append(A[j])

            i += 1
            j += 1

        return ans


if __name__ == '__main__':
    A = [2, 5, 1, 3, 4, 7]
    n = 3
    B = Solution()
    print(B.shuffle(A, n))
