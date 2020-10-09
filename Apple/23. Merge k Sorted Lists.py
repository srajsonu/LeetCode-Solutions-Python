import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, A) -> ListNode:
        n = len(A)
        data = []
        for i in range(n):
            tmp = []
            count = 0
            while A[i]:
                tmp.append((A[i].val, i, count))
                count += 1
                A[i] = A[i].next
            data.append(tmp)
        m = len(data)
        heap = []
        for j in range(n):
            if data[j]:
                heapq.heappush(heap, data[j][0])
        ans = dummy = ListNode(0)
        for i in range(m):
            while heap:
                p, q, r = heapq.heappop(heap)
                ans.next = ListNode(p)
                ans = ans.next
                if r < len(data[q]) - 1:
                    heapq.heappush(heap, data[q][r + 1])
        return dummy.next
