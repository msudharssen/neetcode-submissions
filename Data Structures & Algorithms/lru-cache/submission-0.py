class Node:
    def __init__(self, k: int, v: int):
        self.key = k
        self.value = v
        self.prev = None   
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.keyToNodes = {}
        self.leftNode = Node(0,0)
        self.rightNode = Node(0,0)
        self.leftNode.next = self.rightNode 
        self.rightNode.prev = self.leftNode
    
    def insert(self, node):
        prev = self.rightNode.prev 
        next = self.rightNode
        prev.next = next.prev = node
        node.next = next   
        node.prev = prev

    def remove(self, node):
        prv = node.prev
        nxt = node.next 
        prv.next = nxt   
        nxt.prev = prv 

    def get(self, key: int) -> int:
        if key in self.keyToNodes:
            self.remove(self.keyToNodes[key])
            self.insert(self.keyToNodes[key])
            return self.keyToNodes[key].value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.keyToNodes:
            self.remove(self.keyToNodes[key])
        self.keyToNodes[key] = Node(key, value)
        self.insert(self.keyToNodes[key])

        if len(self.keyToNodes) > self.cap:
            lru = self.leftNode.next 
            self.remove(lru)
            del self.keyToNodes[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)