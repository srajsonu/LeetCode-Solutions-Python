class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int):
        self.s1.append(x)

    def pop(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())

        ans = self.s2.pop()

        while self.s2:
            self.s1.append(self.s2.pop())

        return ans

    def peek(self) -> int:
        return self.s1[0]

    def empty(self) -> bool:
        return True if not self.s1 else False
