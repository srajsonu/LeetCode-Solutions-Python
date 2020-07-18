class Solution:
    def backtrack(self, A, aux):
        if len(A) == 0:
            self.ans.append(aux)
            return

        for i in self.freq[A[0]]:
            self.backtrack(A[1:], aux + i)

    def letterCombinations(self, digits):
        self.ans = []
        self.freq = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.backtrack(digits, "")
        return self.ans if len(digits) != 0 else []

if __name__ == '__main__':
    A = '23'
    B = Solution()
    print(B.letterCombinations(A))
