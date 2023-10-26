class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

#correct solution done on 01-07-2023
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.end = True
            
    
    def search(self, word: str) -> bool:
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.end

    
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True


#this is a revision done on 26-10-2023
class TrieNode:
    def __init__(self):
        self.neighbours = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.neighbours:
                curr.neighbours[char] = TrieNode()
            curr = curr.neighbours[char]
        curr.end = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.neighbours:
                return False
            curr = curr.neighbours[char]
        return curr.end

    def startsWith(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.neighbours:
                return False
            curr = curr.neighbours[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
