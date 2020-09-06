from collections import deque


class Solution:
    def mctFromLeafValues(self, arr) -> int:
        stack = deque()
        stack.append(float('inf'))
        ans = 0

        for ele in arr:
            while stack and stack[-1] <= ele:
                last = stack.pop()
                ans += last * min(stack[-1], ele)
            stack.append(ele)

        while len(stack) > 2:
            ans += stack.pop() * stack[-1]

        return ans
