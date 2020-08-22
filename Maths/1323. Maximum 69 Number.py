class Solution:
    def maximum69Number(self, num: int) -> int:
        num = [i for i in str(num)]
        n = len(num)
        for i in range(n):
            if num[i] == '6':
                num[i] = '9'
                break

        return int(''.join(num))
