class Solution:
    def threeSumClosest(self, nums, target):
        n = len(nums)
        diff = float('inf')
        nums.sort()

        for i in range(n):
            l = i + 1
            h = n - 1

            while l < h:
                sum_ = nums[i] + nums[l] + nums[h]
                if abs(target - sum_) < abs(diff):
                    diff = target - sum_

                if sum_ < target:
                    l += 1
                else:
                    h -= 1

            if diff == 0:
                break

        return target - diff
