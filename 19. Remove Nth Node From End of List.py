class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode: #Two-Pass
        ans = []
        while head:
            ans.append(head.val)
            head = head.next

        m = len(ans)
        idx = m - n
        ans.pop(idx)
        dummy = ListNode()
        tmp = dummy

        while ans:
            tmp.next = ListNode(ans.pop(0))
            tmp = tmp.next

        return dummy.next

    def solve(self, head, n): #One-Pass
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
        i = 0

        while fast.next:
            fast = fast.next
            i += 1

            if i > n:
                slow = slow.next

        slow.next = slow.next.next

        return dummy.next


