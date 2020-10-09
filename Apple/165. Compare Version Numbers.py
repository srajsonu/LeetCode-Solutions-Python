class Solution:
    def solve(self, version1, version2):
        version1 = list(map(int,version1.split('.')))
        version2 = list(map(int,version2.split('.')))

        m = len(version1)
        n = len(version2)

        for i in range(max(m, n)):
            v1 = version1[i] if i < m else 0
            v2 = version2[i] if i < n else 0

            if v1 < v2: return -1
            if v1 > v2: return 1

        return 0

if __name__ == '__main__':
    v1 = '1.01'
    v2 = '1.001'
    v3 = Solution()
    print(v3.solve(v1, v2))
