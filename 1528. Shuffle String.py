class Solution:
    def restoreString(self, s, indices):
        n = len(indices)
        ans = ['' for _ in range(n)]

        for i, j in enumerate(s):
            ans[indices[i]] = j

        return ''.join(ans)


if __name__ == '__main__':
    A = "codeleet"
    B = [4, 5, 6, 7, 0, 2, 1, 3]
    C = Solution()
    print(C.restoreString(A, B))
