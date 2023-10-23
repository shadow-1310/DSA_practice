from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        incoming = defaultdict(list)
        for a,b in edges:
            incoming[b].append(a)

        res = []
        for i in range(n):
            if not incoming[i]:
                res.append(i)

        return res
