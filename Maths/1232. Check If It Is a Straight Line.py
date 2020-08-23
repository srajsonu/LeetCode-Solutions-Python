class Solution:
    def checkStraightLine(self, A) -> bool:
        (x0, y0), (x1, y1) = A[:2]

        for x, y in A:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False

        return True
