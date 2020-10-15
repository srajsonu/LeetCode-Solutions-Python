class Solution:
    def reverseWords(self, s):
        s = s.split(' ')
        n = len(s)
        for i in range(n):
            s[i] = list(s[i])

        for i in range(n):
            s[i] = s[i][::-1]

        for i in range(n):
            s[i] = ''.join(s[i])

        return ' '.join(s)

if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    t = Solution()
    print(t.reverseWords(s))
