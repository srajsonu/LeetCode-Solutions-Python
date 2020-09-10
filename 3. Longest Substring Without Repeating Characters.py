class Solution:
    def solve(self, s):
        n = len(s)
        i, j, ans = 0, 0, 0
        Hash = set()
        while i < n and j < n:
            if s[j] not in Hash:
                Hash.add(s[j])
                ans = max(ans, j - i + 1)
                j += 1
            else:
                Hash.remove(s[i])
                i += 1

        return ans


if __name__ == '__main__':
    A = "abcabcbb"
    B = Solution()
    print(B.solve(A))
