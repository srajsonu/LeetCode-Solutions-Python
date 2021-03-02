class Solution:
    def lengthOfLongestSubstring(self, A):
        n = len(A)
        freq = set()
        i = 0
        j = 0
        max_freq = 0
        while i < n and j < n:
            if A[j] not in freq:
                max_freq = max(max_freq, j - i + 1)
                freq.add(A[j])
                j += 1
            else:
                freq.remove(A[i])
                i += 1

        return max_freq


if __name__ == '__main__':
    A = "pwwkew"
    B = Solution()
    print(B.lengthOfLongestSubstring(A))
