class Solution:
    def countBits(self, num: int):
        ans = []
        for i in range(num+1):
            cnt = 0
            for j in range(32):
                if (i >> j) & 1:
                    cnt += 1
            ans.append(cnt)
        return ans

    def solve(self, num: int):
        ans = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
