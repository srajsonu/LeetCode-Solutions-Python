from typing import List


class Solution:
    def find(self, A, target, l, h):
        mid = (l + h) // 2

        if l > h:
            return h + 1

        if A[mid] == target:
            return mid

        if A[mid] < target:
            return self.find(A, target, mid + 1, h)
        elif A[mid] > target:
            return self.find(A, target, l, mid - 1)

    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        return self.find(nums, target, 0, n - 1)
