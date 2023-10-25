import math
class Solution:
    def numSquares(self, n):
        INF = float('inf')
        cache = [INF]*(n+1)
        cache[0] = 0

        for i in range(1, n+1):
            for j in range(1, int(math.sqrt(i))+1):
                index = i - j**2
                if index >= 0:
                    cache[i] = min(cache[i], 1+cache[index])
                else: 
                    break

        res = cache[n]
        return res 


#this solution is more efficient
#done on 25-10-2023
class Solution:
    def numSquares(self, n):
        INF = float('inf')
        cache = [INF]*(n+1)
        cache[0] = 0

        for target in range(1, n+1):
            for s in range(1, target+1):
                sq = s * s
                if target - sq < 0:
                    break
                cache[target] = min(cache[target], 1+cache[target-sq])

        res = cache[n]
        return res 

s = Solution()
print(s.numSquares(12))
print(s.numSquares(13))
