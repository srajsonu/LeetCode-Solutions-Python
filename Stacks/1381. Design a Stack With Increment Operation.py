from collections import deque


class CustomStack:

    def __init__(self, maxSize: int):
        self.q = deque()
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.q) != self.size:
            self.q.append(x)

    def pop(self) -> int:
        return self.q.pop() if self.q else -1

    def increment(self, k: int, val: int) -> None:
        n = len(self.q)
        if k >= n:
            for i in range(n):
                self.q[i] += val
        else:
            for i in range(k):
                self.q[i] += val
