from collections import deque


class Solution:
    def validateStackSequences(self, A, B):
        stack = deque()
        j = 0
        for i in A:
            stack.append(i)
            while stack and j < len(B) and stack[-1] == B[j]:
                stack.pop()
                j += 1

        return j == len(B)
