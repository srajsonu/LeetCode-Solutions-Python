from heapq import *
class Solution:
    def topKFrequent(self, words, k):
        freq = {}

        for word in words:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

        candidates = list(freq.keys())
        candidates.sort(key=lambda w: (-freq[w], w))
        return candidates[:k]

    def solve(self, words, k):
        freq = {}
        for w in words:
            if w not in freq:
                freq[w] = 1
            else:
                freq[w] += 1

        heap = [(-cnt, word) for word, cnt in freq.items()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]

if __name__ == '__main__':
    w = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    s = Solution()
    print(s.topKFrequent(w, k))
    print(s.solve(w, k))
