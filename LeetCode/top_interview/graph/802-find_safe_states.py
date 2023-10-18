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


#revision done on 18-10-2023
class Solution:
    def eventualSafeNodes(self, graph):
        visited = set()
        safe = set()
        res = []
        def dfs(i):
            if i in safe:
                return True
            if i in visited:
                return False

            visited.add(i)
            if len(graph[i])==0:
                safe.add(i)
                return True
            for nei in graph[i]:
                if not dfs(nei):
                    return False
                safe.add(nei)
            visited.remove(i)
            safe.add(i)

            return True

        for i in range(len(graph)):
            if dfs(i):
                res.append(i)

        return res

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
s = Solution()
print(s.eventualSafeNodes(graph))
