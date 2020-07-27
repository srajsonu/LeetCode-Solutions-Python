class Solution:
    def Solve(self,l,h):
        if l%2 != 0 or h%2 != 0:
            return (h-l)//2 + 1
        if l%2 == 0 and h%2 == 0:
            return (h-l)//2

if __name__ == '__main__':
    l = 3
    h = 7
    C = Solution()
    print(C.Solve(l,h))
