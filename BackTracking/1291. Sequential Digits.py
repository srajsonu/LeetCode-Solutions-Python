class Solution:
    def Solve(self,low,high):
        ans = []
        for i in range(1,10):
            num = i
            next = i
            while num <= high and next < 10:
                if num >= low:
                    ans.append(num)
                next += 1
                num = num * 10 + next
        return sorted(ans)

if __name__ == '__main__':
    A = 100
    B = 300
    C = Solution()
    print(C.Solve(A,B))
