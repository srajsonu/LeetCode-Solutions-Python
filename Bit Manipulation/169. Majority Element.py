from typing import List


class Solution:
    def majorityElement(self, A: List[int]) -> int:
        n = len(A)
        major = A[0]
        cnt = 1

        for i in range(1, n):
            if major == A[i]:
                cnt += 1

            elif cnt == 0:
                cnt += 1
                major = A[i]
            else:
                cnt -= 1

        return major
