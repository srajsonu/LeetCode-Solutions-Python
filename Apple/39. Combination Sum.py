from typing import List


class Solution:
    def combination(self, A, sum_, i, cur_sum):
        if sum(cur_sum) > sum_:
            return 0

        if i == len(A):
            if sum(cur_sum) == sum_:
                self.ans.append(cur_sum)
            return

        take = self.combination(A, sum_, i, cur_sum + [A[i]])
        dont = self.combination(A, sum_, i + 1, cur_sum)
        return take and dont

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.combination(candidates, target, 0, [])
        return self.ans
