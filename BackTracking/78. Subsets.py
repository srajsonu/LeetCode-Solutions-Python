from typing import List
class Solution:
    def generate(self, A, index, aux):
        if index == len(A):
            self.ans.append(aux)
            return

        pick = self.generate(A, index + 1, aux + [A[index]])
        dont = self.generate(A, index + 1, aux)
        return pick and dont

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.generate(nums, 0, [])
        return self.ans

if __name__ == '__main__':
    A = [1,2,3]
    B = Solution()
    print(B.subsets(A))
