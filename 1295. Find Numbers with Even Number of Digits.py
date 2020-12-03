class Solution:
    def findNumbers(self, nums):
        cnt = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                cnt += 1

        return cnt

if __name__ == '__main__':
    A = [12, 345, 2, 6, 7896]
    B = Solution()
    print(B.findNumbers(A))
