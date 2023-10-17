from collections import deque
#this solution will not work here as the graph is directed , following approach is wrong
class Solution:
    def possibleBipartition(self, n, dislikes):
        adj_list = [ [] for i in range(n+1)]
        for a,b in dislikes:
            adj_list[a].append(b)
            adj_list[b].append(a)
        print(adj_list)
        
        group = [0] * (n+1)
        def bfs(i):
            if group[i]:
                return True
            q = deque()
            q.append(i)
            group[i] = 1

            while q:
                curr = q.popleft()
                for nei in adj_list[curr]:
                    if group[nei] and group[nei] == group[curr]:
                        return False
                    elif not group[nei]:
                        group[nei] = -group[curr]
                        q.append(nei)

            return True
        for i in range(1, n+1):
            if not bfs(i):
                return False

        return True

n = 4; dislikes = [[1,2],[1,3],[2,4]]
s = Solution()
print(s.possibleBipartition(n, dislikes))
n = 3; dislikes = [[1,2],[1,3],[2,3]]
print(s.possibleBipartition(n, dislikes))
