class Solution:
    def balancedStringSplit(self, s):
        ans = cnt = 0

        for c in s:
            if c == 'L':
                cnt += 1
            else:
                cnt -= 1

            if cnt == 0:
                ans += 1

        return ans

if __name__ == '__main__':
    A = "RLRRLLRLRL"
    B = Solution()
    print(B.balancedStringSplit(A))
