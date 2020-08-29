class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in dic:
                top = stack.pop() if stack else -1
                if dic[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack
