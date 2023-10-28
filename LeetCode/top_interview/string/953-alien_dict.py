class Solution:
    def isAlienSorted(self, words, order):
        order_map = {c:i for i, c in enumerate(order)}
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    break

        return True
    

#this revision was done on 28-10-2023
class Solution:
    def isAlienSorted(self, words, order):
        word_order = {char: index for index, char in enumerate(order)}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if word_order[word1[j]] > word_order[word2[j]]:
                        return False
                    break

        return True

words = ["hello","leetcode"]; order = "hlabcdefgijkmnopqrstuvwxyz"   
s = Solution()
print(s.isAlienSorted(words, order))

