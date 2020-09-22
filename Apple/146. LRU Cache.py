class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.size = capacity
        self.D = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.D:
            return -1

        n = self.D[key]
        self.remove(n)
        self.add(n)
        return n.val

    def put(self, key, val):
        if key in self.D:
            self.remove(self.D[key])
            del self.D[key]

        elif len(self.D) == self.size:
            n = self.head.next
            self.remove(n)
            del self.D[n.key]

        n = Node(key, val)
        self.D[key] = n
        self.add(n)

    def add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        p = node.prev
        p.next = node.next
        node.next.prev = p


from collections import OrderedDict
class LRU: #Shortest form

    def __init__(self, capacity):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)
