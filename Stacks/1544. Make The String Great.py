class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            tmp = ord(i)
            if stack and (ord(stack[-1]) == tmp + 32 or ord(stack[-1]) == tmp - 32):
                stack.pop()
            else:
                stack.append(i)

        return ''.join(stack)
