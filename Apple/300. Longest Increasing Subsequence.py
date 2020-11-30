class Solution:
    def dp(self, A, idx, prev, dp): #O(n^2)
        if idx == len(A):
            return 0

        key = str(idx) + str(prev)
        if key in dp:
            return dp[key]

        pick = 0
        if prev < 0 or A[idx] > A[prev]:
            pick = 1 + self.dp(A, idx + 1, idx, dp)

        dont = self.dp(A, idx+1, prev, dp)
        dp[key] = max(pick, dont)
        return dp[key]

    def lengthOfLIS(self, nums):
        dp = {}
        return self.dp(nums, 0, -1, dp)

    def solve(self, nums): #O(nlogn)
        n = len(nums)
        dp = [0 for _ in range(n)]
        ans = 0
        for num in nums:
            i = 0
            j = ans

            while i != j:
                mid = (i + j) // 2
                if dp[mid] < num:
                    i = mid + 1
                else:
                    j = mid

            dp[i] = num
            ans = max(i + 1, ans)

        return ans


if __name__ == '__main__':
    A = [4,10,4,3,8,9]
    B = Solution()
    print(B.lengthOfLIS(A))
    print(B.solve(A))
