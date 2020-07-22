class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.ans = []
        self.backtrack(characters, combinationLength, 0, [])
        self.i = 0

    def backtrack(self, A, B, index, aux):
        if index == len(A):
            if len(aux) == B:
                self.ans.append("".join(aux))
            return

        pick = self.backtrack(A, B, index + 1, aux + [A[index]])
        dont = self.backtrack(A, B, index + 1, aux)
        return pick and dont

    def next(self) -> str:
        ans = self.ans[self.i]
        self.i += 1
        return ans

    def hasNext(self) -> bool:
        n = len(self.ans)
        if self.i < n:
            return True
        else:
            return False

if __name__ == '__main__':
    A = 'abc'
    B = 2
    C = CombinationIterator(A,B)
    print(C.next())
    print(C.hasNext())
