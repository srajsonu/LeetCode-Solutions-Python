class Solution:
    def missingNumber(self, nums):
        n = len(nums) + 1
        missing = set(nums)
        for i in range(n):
            if i not in missing:
                return i
