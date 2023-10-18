from collections import defaultdict
class Solution:
    def findCenter(self, edges):
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        res = [0,0]
        for key in graph:
            if len(graph[key]) > res[1]:
                res[0] = key
                res[1] = len(graph[key])

        return res[0]

#this is a optimized approach
class Solution:
    def findCenter(self, edges):
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]


edges1 = [[1,2],[5,1],[1,3],[1,4]]
edges2 = [[1,2],[2,3],[4,2]]
s = Solution()
print(s.findCenter(edges1))
print(s.findCenter(edges2))
