from collections import deque


class Solution:
    def ladderLength(self, A, B, C):
        C = set(C)
        q = deque()
        q.append((A, 0))

        while q:
            tmp = []
            word, depth = q.popleft()
            tmp.append(word)
            if word == B:
                return depth + 1

            word = [i for i in word]
            for i in range(len(word)):
                tmp = word[i]
                for j in range(ord('a'), ord('z')+1):
                    if tmp == chr(j):
                        continue
                    word[i] = chr(j)

                    new_word = "".join(word)
                    if new_word in C:
                        C.remove(new_word)
                        q.append((new_word, depth+1))
                word[i] = tmp

        return -1


if __name__ == '__main__':
    A = "hit"
    B = "cog"
    C = ["hot","dot","dog","lot","log","cog"]
    D = Solution()
    print(D.ladderLength(A, B, C))
