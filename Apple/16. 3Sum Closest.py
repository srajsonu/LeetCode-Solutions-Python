class Solution:
    def threeSumClosest(self, A, B):
        n = len(A)
        A.sort()

        ans = A[0] + A[1] + A[2]
        for i in range(n-2):
            j = i + 1
            k = n - 1

            while j < k:
                sm = A[i] + A[j] + A[k]
                if sm == B:
                    return sm

                if abs(sm - B) < abs(ans - B):
                    ans = sm

                elif sm < B:
                    j += 1
                elif sm > B:
                    k -= 1

        return ans


if __name__ == '__main__':
    A = [-1, 2, 1, -4]
    B = 1
    C = Solution()
    print(C.threeSumClosest(A, B))
