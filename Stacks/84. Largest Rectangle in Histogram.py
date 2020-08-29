from collections import deque


class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        n = len(height)
        stack = deque()
        stack.append(-1)
        ans = 0
        for i in range(n):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans
