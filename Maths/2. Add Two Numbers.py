class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import deque


class Solution:
    def dfs1(self, root):
        if not root:
            return
        self.val1.appendleft(str(root.val))
        self.dfs1(root.next)

    def dfs2(self, root):
        if not root:
            return
        self.val2.appendleft(str(root.val))
        self.dfs2(root.next)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.val1 = deque()
        self.val2 = deque()
        self.dfs1(l1)
        self.dfs2(l2)
        ans = int(''.join(self.val1)) + int(''.join(self.val2))
        ans = [i for i in str(ans)][::-1]

        dummy = ListNode()
        node = dummy
        while ans:
            tmp = ans.pop(0)
            node.next = ListNode(int(tmp))
            node = node.next

        return dummy.next
