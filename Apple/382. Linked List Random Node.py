from random import randint


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: ListNode):
        self.root = head

    def getRandom(self) -> int:
        head = self.root
        ans = []
        while head:
            ans.append(head.val)
            head = head.next

        return ans[randint(0, len(ans) - 1)]
