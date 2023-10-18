from collections import deque

#it is a bfs approach done on 2023-10-01, working on all LC testcases
class Solution:
    def cloneGraph(self, node):
        q = deque()
        hashmap = {}
        q.append(node)
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr in hashmap or not curr:
                    continue
                hashmap[curr] = Node()
                neighbors = curr.neighbors
                for n in neighbors:
                    q.append(n)

        for key in hashmap:
            hashmap[key].val = key.val
            for n in key.neighbors:
                hashmap[key].neighbors.append(hashmap[n])

        return hashmap[key] if node else None


#this revision done on 17-10-2023
class Solution:
    def cloneGraph(self, node):
        q = deque()
        clone_map = {}
        q.append(node)

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr in clone_map or not curr:
                    continue
                clone_map[curr] = Node()
                for nei in curr.neighbors:
                    q.append(nei)

        for key in clone_map:
            clone_map[key].val = key.val
            for nei in key.neighbors:
                clone_map[key].neighbors.append(clone_map[nei])

        return clone_map[node] if node else None
