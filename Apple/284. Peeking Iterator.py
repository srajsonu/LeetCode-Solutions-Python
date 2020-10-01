class PeekingIterator:
    def __init__(self, iterator):
        self.val = iterator
        self.tmp = self.val.next() if self.val.hasNext() else None

    def peek(self):
        return self.tmp

    def next(self):
        ans = self.tmp
        self.tmp = self.val.next() if self.val.hasNext() else None
        return ans

    def hasNext(self):
        return self.tmp is not None
    
