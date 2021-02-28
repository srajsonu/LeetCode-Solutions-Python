class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        if not l1 and not l2:
            return

        if not l1:
            return l2

        if not l2:
            return l1

        t1 = l1
        t2 = l2

        if t1.val > t2.val:
            t1, t2 = t2, t1

        l1 = t1

        while t1.next and t2:
            if t1.val <= t2.val and t1.next.val <= t2.val:
                t1 = t1.next
            elif t1.val <= t2.val:
                tmp = t2
                t2 = t1.next
                t1.next = tmp

        if not t1.next:
            t1.next = t2

        return l1
