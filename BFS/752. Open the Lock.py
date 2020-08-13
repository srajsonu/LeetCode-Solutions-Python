from collections import deque
class Solution:
    def Solve(self,A,B):
        dic = set()
        for i in A:
            dic.add(i)

        vis = set()
        q = deque()
        q.append(('0000', 0))
        vis.add('0000')

        while q:
            string, level = q.popleft()
            if string == B:
                return level

            elif string in dic:
                continue

            for i in range(4):
                digit = int(string[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_string = string[:i] + str(new_digit) + string[i + 1:]
                    if new_string not in vis:
                        vis.add(new_string)
                        q.append((new_string, level + 1))

        return -1

if __name__ == '__main__':
    A = ["0201", "0101", "0102", "1212", "2002"]
    B = "0202"
    C = Solution()
    print(C.Solve(A,B))
