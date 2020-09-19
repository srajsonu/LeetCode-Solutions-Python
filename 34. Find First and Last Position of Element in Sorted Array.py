from typing import List


class Solution:
    def search(self, A, target, l, h):
        mid = (l + h) // 2

        if l > h: return -1

        if A[mid] == target:
            return mid

        if A[mid] < target:
            return self.search(A, target, mid + 1, h)

        elif A[mid] > target:
            return self.search(A, target, l, mid - 1)

    def searchRange(self, A: List[int], target: int) -> List[int]:
        n = len(A)
        if n == 1:
            if A[0] != target:
                return [-1, -1]
            else:
                return [0, 0]

        s = self.search(A, target, 0, n - 1)
        if s == -1:
            return [-1, -1]

        l = s
        h = s

        while l > 0 and A[l] == A[l - 1]:
            l -= 1

        while h < n - 1 and A[h] == A[h + 1]:
            h += 1

        return [l, h]
