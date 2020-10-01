from heapq import *


class MedianFinder:
    def __init__(self):
        self.mx = []
        self.mn = []

    def addNum(self, num: int) -> None:
        m = len(self.mx)
        n = len(self.mn)

        if m == n:
            heappush(self.mx, -num)
            heappush(self.mn, -heappop(self.mx))
        else:
            heappush(self.mn, num)
            heappush(self.mx, -heappop(self.mn))

    def findMedian(self) -> float:
        m = len(self.mn)
        n = len(self.mx)

        if m == n:
            b = heappop(self.mn)
            c = -heappop(self.mx)
            med = (b + c) / 2
            heappush(self.mn, b)
            heappush(self.mx, -c)
            return med

        elif m < n:
            b = -heappop(self.mx)
            heappush(self.mx, -b)
            return b

        elif m > n:
            b = heappop(self.mn)
            heappush(self.mn, b)
            return b
