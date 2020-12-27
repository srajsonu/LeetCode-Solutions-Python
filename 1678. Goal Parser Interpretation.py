class Solution:
    def interpret(self, s):
        return s.replace('()', 'o').replace('(al)', 'al')

if __name__ == '__main__':
    s = 'G()(al)'
    t = Solution()
    print(t.interpret(s))
