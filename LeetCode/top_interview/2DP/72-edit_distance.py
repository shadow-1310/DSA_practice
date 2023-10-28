class Solution: 
    def minDistance(self, word1, word2):
        INF = float('inf')
        cache = [ [INF]*(len(word2)+1) for i in range(len(word1)+1) ] 

        for i in range(len(word1)+1):
            cache[i][-1] = len(word1) - i

        for i in range(len(word2)+1):
            cache[-1][i] = len(word2) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]

                else:
                    cache[i][j] = 1 + min( 
                                            cache[i+1][j],
                                            cache[i][j+1],
                                            cache[i+1][j+1]
                                        )
        return cache[0][0]


#revision done on 28-10-2023
class Solution:
    def minDistance(self, word1, word2):
        n1 = len(word1)
        n2 = len(word2)
        cache = [ [0]*(n2+1) for i in range(n1+1) ] 
        for i in range(n1):
            cache[i][-1] = n1 - i 
        for i in range(n2):
            cache[-1][i] = n2 - i

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j+1], cache[i+1][j], cache[i][j+1])

        return cache[0][0]

word1 = 'horse'
word2 = 'ros'
# word1 = 'intention'
# word2 = 'execution'
s = Solution()
print(s.minDistance(word1, word2))
