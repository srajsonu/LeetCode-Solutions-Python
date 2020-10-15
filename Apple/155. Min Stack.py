from heapq import *


class MinStack:

    def __init__(self):
        self.pq = []
        self.ans = []

    def push(self, x: int) -> None:
        heappush(self.pq, x)
        self.ans.append(x)

    def pop(self) -> None:
        tmp = self.ans.pop()

        ans = []
        while self.pq:
            val = heappop(self.pq)
            if val == tmp:
                break
            ans.append(val)

        while ans:
            heappush(self.pq, ans.pop())

    def top(self) -> int:
        return self.ans[-1]

    def getMin(self) -> int:
        tmp = heappop(self.pq)
        heappush(self.pq, tmp)
        return tmp
