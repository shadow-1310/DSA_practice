class Solution:
    def eventualSafeNodes(self, graph):
        safe = set()
        res = []
        visited = set()
        def dfs(node):
            if node in safe:
                return True

            if graph[node] == []:
                safe.add(node)
                return True
            if node in visited:
                return False

            visited.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited.remove(node)

            return True

        for i in range(len(graph)):
            if dfs(i):
                res.append(i)

        return res
