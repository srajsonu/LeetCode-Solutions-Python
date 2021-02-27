class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val > l2.val:
            l1, l2 = l2, l1

        curr1 = l1
        curr2 = l2

        while curr1.next and curr2:
            if curr1.val <= curr2.val and curr1.next.val <= curr2.val:
                curr1 = curr1.next
            elif curr1.val <= curr2.val:
                curr2, curr1.next = curr1.next, curr2

        if curr1.next:
            curr1.next = curr2

        return l1
