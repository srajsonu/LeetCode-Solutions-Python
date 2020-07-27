class NumArray:
    def __init__(self, nums):
        self.A = nums

    def sumRange(self, i: int, j: int):
        return sum(self.A[i:j + 1])

if __name__ == '__main__':
    A = [-2, 0, 3, -5, 2, -1]
    B = NumArray(A)
    print(B.sumRange(0,2))
