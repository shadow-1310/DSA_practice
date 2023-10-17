from collections import deque
class Solution:
    def isBipartite(self, graph):
        color = [0]*(len(graph)+1)
        def bfs(i):
            if color[i]:
                return True
            q = deque()
            q.append(i)
            color[i] = 1

            while q:
                curr = q.popleft()
                for nei in graph[curr]:
                    if color[nei] and color[curr] == color[nei]:
                        return False
                    elif not color[nei]:
                        q.append(nei)
                        color[nei] = -color[curr]

            return True

        for i in range(len(graph)):
            if not bfs(i):
                return False

        return True

graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
s = Solution()
print(s.isBipartite(graph))
