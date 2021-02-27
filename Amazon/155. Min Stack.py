class MinStack:

    def __init__(self):
        self.stack = []
        self.mn = 0
        self.cnt = 0

    def push(self, x: int) -> None:
        if not self.stack:
            self.mn = x
            self.stack.append(x)
        elif x < self.mn:
            val = (2 * x) - self.mn
            self.stack.append(val)
            self.mn = x
        else:
            self.stack.append(x)

        self.cnt += 1

    def pop(self) -> None:
        if self.stack:
            tmp = self.stack.pop()
            if tmp < self.mn:
                val = (2 * self.mn) - tmp
                self.mn = val

            if not self.stack:
                self.mn = -1

            self.cnt -= 1
        else:
            self.mn = -1

    def top(self) -> int:
        if self.stack:
            val = self.stack[self.cnt - 1]
            if val < self.mn:
                return self.mn
            else:
                return val
        else:
            return -1

    def getMin(self) -> int:
        return self.mn
