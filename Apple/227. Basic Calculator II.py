class Solution:
    def calculate(self, s):
        n = len(s)
        stack = []
        num = 0
        sign = '+'
        dic = {'+', '-', '*', '/'}

        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if s[i] in dic or i == n-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))

                num = 0
                sign = s[i]

        return sum(stack)

if __name__ == '__main__':
    s = "14-3/2"
    t = Solution()
    print(t.calculate(s))
