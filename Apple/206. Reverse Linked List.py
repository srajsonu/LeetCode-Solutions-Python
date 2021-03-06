class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        tmp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tmp

    def solve(self, head):
        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

if __name__ == '__main__':
    A = []
    B = Solution()
    print(B.solve(A))
