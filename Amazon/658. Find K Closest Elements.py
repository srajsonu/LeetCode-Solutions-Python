from collections import defaultdict


class Solution:
    def findClosestElements(self, A, B, C):
        n = len(A)
        freq = defaultdict(list)
        for i in range(n):
            idx = abs(C - A[i])
            freq[idx].append(A[i])

        freq = sorted(freq.items())
        ans = []
        for i, j in freq:
            for k in j:
                if len(ans) == B:
                    break
                ans.append(k)

        return sorted(ans)

    def solve(self, A, B, C):
        n = len(A)
        l = 0
        h = n-B

        while l < h:
            mid = (l + h) // 2
            if C - A[mid] > A[mid+B] - C:
                l = mid + 1
            else:
                h = mid

        return A[l:h+B]


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = 4
    C = 3
    D = Solution()
    print(D.findClosestElements(A, B, C))
    print(D.solve(A, B, C))
