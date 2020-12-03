class Solution:
    def moveZeroes(self, nums):
        zeros = []
        while 0 in nums:
            nums.remove(0)
            zeros.append(0)
        nums.extend(zeros)

        return nums

if __name__ == '__main__':
    A = [0,1,0,3,12]
    B = Solution()
    print(B.moveZeroes(A))
