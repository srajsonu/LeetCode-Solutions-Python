class Solution:
    def solve(self, nums):
        curr_sum = 0
        max_sum = 0

        for num in nums:
            curr_sum = max(0, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum

    def maxSubarray(self, nums):
        curr_sum = 0
        max_sum = 0
        s = e = 0

        for curr_end,j in enumerate(nums):
            global curr_start
            if curr_sum <= 0:
                curr_start = curr_end
                curr_sum = j

            else:
                curr_sum += j

            if curr_sum > max_sum:
                max_sum = curr_sum
                s = curr_start
                e = curr_end + 1

        return max_sum, s, e


if __name__ == '__main__':
    A = [1, 8, -2, 1, 2, 3]
    B = Solution()
    print(B.solve(A))
    print(B.maxSubarray(A))
