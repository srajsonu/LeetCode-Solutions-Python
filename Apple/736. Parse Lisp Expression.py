class Solution:
    def evaluate(self, token):
        n = len(token)
        if token[0] in ('add', 'mult'):
            n1, n2 = int(self.d.get(token[1], token[1])), int(self.d.get(token[2], token[2]))
            return str(n1 + n2) if token[0] == 'add' else str(n1 * n2)

        else:
            for i in range(1, n-2, 2):
                self.d[token[i]] = self.d.get(token[i+1], token[i+1])

            return self.d.get(token[-1], token[-1])

    def solve(self, exp):
        stack = []
        self.d = {}
        token = ['']

        for c in exp:
            if c == '(':
                if token[0] == 'let':
                    self.evaluate(token)

                stack.append((token, dict(self.d)))
                token = ['']

            elif c == ')':
                val = self.evaluate(token)
                token, self.d = stack.pop()
                token[-1] += val

            elif c == ' ':
                token.append('')

            else:
                token[-1] += c

        return int(token[0])

if __name__ == '__main__':
    s = '(add 1 2)'
    t = Solution()
    print(t.solve(s))
