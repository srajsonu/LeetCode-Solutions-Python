class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def build(self,start,end):
        ans = []

        if start > end:
            ans.append(None)
            return ans

        if start == end:
            ans.append(TreeNode(start))
            return ans

        for i in range(start,end+1):
            left = self.build(start,i-1)
            right = self.build(i+1,end)

            for lNode in left:
                for rNode in right:
                    root = TreeNode(i)
                    root.left = lNode
                    root.right = rNode
                    ans.append(root.val)

            return ans

    def Solve(self,A):
        return self.build(1,A)

if __name__ == '__main__':
    A = 5
    B = Solution()
    print(B.Solve(A))
