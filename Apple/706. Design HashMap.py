class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.m = 1000
        self.hash = [None for _ in range(self.m)]

    def put(self, key, val):
        index = key % self.m

        if not self.hash[index]:
            self.hash[index] = ListNode(key, val)
        else:
            curr = self.hash[index]
            while True:
                if curr.key == key:
                    curr.key = key
                    curr.val = val
                    return

                if not curr.next: break
                curr = curr.next

            curr.next = ListNode(key, val)

    def get(self, key):
        index = key % self.m
        curr = self.hash[index]

        while curr:
            if curr.key == key:
                return curr.val

            curr = curr.next

        return -1

    def remove(self, key):
        index = key % self.m
        prev = curr = self.hash[index]

        if not curr: return
        if curr.key == key:
            self.hash[index] = curr.next

        else:
            curr = curr.next

            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    break
                curr, prev = curr.next, prev.next
