from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.end = True

    def search(self, word):
        curr = self.root
        
        for i,char in enumerate(word):

            if char not in curr.children:
                return False
            
            if curr.end and self.search(word[i+1:]):
                return True
            
            curr = curr.children[char]    
    
# this solution is not passing all the test cases, for some it is showing time limit exceed
#done on 02-07-2023
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = Trie()
        
        for word in wordDict:
            dic.add_word(word)

        return dic.search(s)


#this is a correct solution using DP
#done on 26-10-2023
class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s)
        cache = [False] * (n+1)
        cache[n] = True

        for i in range(n-1, -1, -1):
            for word in wordDict:
                w = len(word)
                if i + w <= n and s[i:i+w] == word:
                    cache[i] = cache[i+w]

                if cache[i]:
                    break

        return cache[0]
