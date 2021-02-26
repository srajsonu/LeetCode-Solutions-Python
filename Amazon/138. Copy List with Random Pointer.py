class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head: return head
        curr = head

        # Copy of new node
        while curr:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = curr.next.next

        # Copy of random node
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        dup_node = head.next

        while curr.next:
            tmp = curr.next
            curr.next = curr.next.next
            curr = tmp

        return dup_node
