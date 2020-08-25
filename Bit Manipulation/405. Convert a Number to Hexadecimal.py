class Solution:
    def solve(self, num):
        ans = []
        dic = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f'
        }

        if num == 0:
            return '0'

        if num < 0:
            num += 2 ** 32

        while num:
            dig = num % 16
            num = (num -  dig)//16
            if dig > 9 and dig < 16:
                dig = dic[dig]
            else:
                dig = str(dig)

            ans.append(dig)

        return "".join(ans)

if __name__ == '__main__':
    num = 26
    A = Solution()
    print(A.solve(num))
