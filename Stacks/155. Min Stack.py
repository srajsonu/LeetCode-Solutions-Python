from collections import deque


class MinStack:

    def __init__(self):
        self.q = deque()
        self.mn = []

    def push(self, x: int) -> None:
        if not self.q:
            self.q.append(x)
            self.mn.append(x)
        else:
            self.q.append(x)
            if self.mn[-1] < x:
                self.mn.append(self.mn[-1])
            else:
                self.mn.append(x)

    def pop(self) -> None:
        self.q.pop() if self.q else -1
        self.mn.pop() if self.mn else -1

    def top(self) -> int:
        return self.q[-1] if self.q else -1

    def getMin(self) -> int:
        return self.mn[-1] if self.mn else -1
