from typing import List
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for t in tasks:
            if t in counts:
                counts[t] += 1
            else:
                counts[t] = 1

        freq = [-c for c in counts.values()]
        heapq.heapify(freq)
        q = deque()
        t = 0

        while freq or q:
            t += 1
            
            if freq:
                task = heapq.heappop(freq)
                task += 1
            
                if task:
                    q.append([task, t+n])
            
            if q and q[0][1] == t:
                new = q.popleft()[0]
                heapq.heappush(freq, new)

        return t