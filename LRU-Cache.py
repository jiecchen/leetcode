from collections import deque

class Node:
    def __init__(self, key, val):
        self._active = True
        self.val = val
        self.key = key

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self._cap = capacity
        self._dq = deque()
        self._dict = {}
        self._size = 0

    # @return an integer
    def get(self, key):
        if key in self._dict:
            node = self._dict[key]
            self._moveToHead(key)
            return node.val
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self._dict:
            node = self._dict[key]
            node.val = value
            self._moveToHead(key)
        else:
            if self._size >= self._cap:
                node = self._dq.popleft()
                while not node._active:
                    node = self._dq.popleft()
                del self._dict[node.key]
                self._size -= 1
            node = Node(key, value)
            self._dq.append(node)
            self._dict[key] = node
            self._size += 1

    def _moveToHead(self, key):
        tmp = self._dict[key]
        node = Node(tmp.key, tmp.val)
        self._dq.append(node)
        tmp._active = False
        self._dict[key] = node

