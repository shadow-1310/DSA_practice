from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph):
        q = deque()
        n = len(graph)-1
        res = []
        def dfs(node, path):
            if node == n:
                path.append(node)
                res.append(path[:])
                path.pop()
                return
            for nei in graph[node]:
                path.append(node)
                dfs(nei, path)
                path.pop()
        dfs(0, [])
        return res

graph = [[1,2],[3],[3],[]]
s = Solution()
print(s.allPathsSourceTarget(graph))

