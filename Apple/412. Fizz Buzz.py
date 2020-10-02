from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [str(i) for i in range(1, n + 1)]

        for i in range(n):
            if (i + 1) % 3 == 0:
                ans[i] = 'Fizz'

            if (i + 1) % 5 == 0:
                ans[i] = 'Buzz'

            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                ans[i] = 'FizzBuzz'

        return ans
