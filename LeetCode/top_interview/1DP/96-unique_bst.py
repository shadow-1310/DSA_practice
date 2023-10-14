#this solution was done on 2023-10-11
class Solution:
    def numTrees(self, n):
        cache = [1]*(n+1)
        for nodes in range(2, n+1):
            total = 0
            for root in range(1, nodes+1):
                left = root -1
                right = nodes - root
                total += cache[left]*cache[right]
            cache[nodes] = total

        return cache[n]

s = Solution()
print(s.numTrees(3))
