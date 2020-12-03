class Solution:
    def createTargetArray(self, nums, index):
        m = len(nums)
        ans = []

        for i in range(m):
            ans.insert(index[i], nums[i])

        return ans


if __name__ == '__main__':
    A = [0, 1, 2, 3, 4]
    B = [0, 1, 2, 2, 1]
    C = Solution()
    print(C.createTargetArray(A, B))
