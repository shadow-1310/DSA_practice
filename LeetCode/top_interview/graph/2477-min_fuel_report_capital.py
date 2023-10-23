from math import ceil
from collections import defaultdict
class Solution:
    def minimumFuelCost(self, roads, seats):
        adj = defaultdict(list)
        for src, des in roads:
            adj[src].append(des)
            adj[des].append(src)

        res = 0
        def dfs(node, parent):
            nonlocal res
            passangers = 0
            for child in adj[node]:
                if child != parent:
                    p = dfs(child, node)
                    passangers += p
                    res += int(ceil(p/seats))
            return passangers + 1

        dfs(0, -1)
        return res

roads = [[0,1],[0,2],[0,3]]
seats = 5
s = Solution()
print(s.minimumFuelCost(roads, seats))
roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
seats = 2
print(s.minimumFuelCost(roads, seats))
