class TreeNode:

    def __init__(self):
        self.children=defaultdict()
        self.endOfWord=False

class PrefixTree:

    def __init__(self):
        self.curre=TreeNode()
        

    def insert(self, word: str) -> None:
        curr = self.curre
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TreeNode()
            curr = curr.children[ch]
        curr.endOfWord=True
        
    
    def search(self, word: str) -> bool:
        curr = self.curre
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.curre
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr=curr.children[ch]
        return True        
        