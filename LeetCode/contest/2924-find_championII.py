#it is a contest problem 
#done on 05-11-2023
class Solution:
    def findChampion(self, n, edges):
        pointers = [ [] for i in range(n)]
        res = []
        for a,b in edges:
            pointers[b].append(a)
        
        for i in range(n):
            if not pointers[i]:
                res.append(i)

        return res[-1] if len(res) == 1 else -1

n = 4; edges = [[0,2],[1,3],[1,2]]
n = 3; edges = [[0,1],[1,2]]
s = Solution()
print(s.findChampion(n, edges))

