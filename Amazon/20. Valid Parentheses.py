class Solution:
    def isValid(self, A):
        stack = []
        for i in A:
            if i == '}' or i == ']' or i == ')':
                if not stack:
                    return False

                if stack[-1] != '(' and i == ')':
                    return False

                if stack[-1] != '{' and i == '}':
                    return False

                if stack[-1] != '[' and i == ']':
                    return False

                stack.pop()
            else:
                stack.append(i)

        return not stack


if __name__ == '__main__':
    A = "(])"
    B = Solution()
    print(B.isValid(A))
