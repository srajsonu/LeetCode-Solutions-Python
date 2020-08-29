from collections import deque
from traitlets import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        stack = deque()
        ans = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right

        return ans
