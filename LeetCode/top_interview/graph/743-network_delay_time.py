import heapq
import collections
class Solution:
    def networkDelayTime(self, times, n, k):
        adj_list = collections.defaultdict(list)
        for s,d,w in times:
            adj_list[s].append((d,w))
        
        # while using self implementation of defaultdict it is not working
        # adj_list = {}
        # for s,d,w in times:
        #     if s not in adj_list:
        #         adj_list[s] = [(d,w)]
        #     else:
        #         adj_list[s].append((d,w))

        min_heap = [(0, k)]
        visited = set()
        t = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
               continue
            visited.add(n1)
            t = max(t, w1)

            for n2, w2 in adj_list[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1+w2, n2))
            
        return t if len(visited) == n else -1


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
s = Solution()
print(s.networkDelayTime(times, n, k))
