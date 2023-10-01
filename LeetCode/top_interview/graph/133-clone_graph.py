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
                if curr in hashmap:
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
