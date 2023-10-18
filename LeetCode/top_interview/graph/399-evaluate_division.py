from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations, values, queries):
        adj_list = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj_list[a].append([b, values[i]])
            adj_list[b].append([a, 1 / values[i]])

        def dfs(src, target):
            if src not in adj_list or target not in adj_list:
                return -1
            visited = set()
            q = deque()
            q.append([src, 1])

            while q:
                n1, w1 = q.popleft()
                if n1 == target:
                    return w1
                visited.add(n1)
                for n2, w2 in adj_list[n1]:
                    if n2 not in visited:
                        visited.add(n2)
                        q.append([n2, w1*w2])
            return -1

        return [dfs(a, b) for a,b in queries]


#revision done on 18-10-2023
class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)
        for idx, var in enumerate(equations):
            a = var[0]
            b = var[1]
            graph[a].append([b, values[idx]])
            graph[b].append([a, 1 / values[idx]])

        def bfs(src, target):
            if src not in graph or target not in graph:
                return -1
            visited = set()
            q = deque()
            q.append([src, 1])
            while q:
                n1, w1 = q.popleft()
                if n1 == target:
                    return w1
                for n2,w2 in graph[n1]:
                    if n2 not in visited:
                        visited.add(n2)
                        q.append([n2,w1*w2])

            return -1

        return [bfs(src, target) for src, target in queries]

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
s = Solution()
print(s.calcEquation(equations,values, queries))
