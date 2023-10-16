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


class Solution:
    def leastInterval(self, tasks, n):
        counts = {}
        for t in tasks:
            if t in counts:
                counts[t] += 1
            else:
                counts[t] = 1

        freq = [-n for n in counts.values()]
        heapq.heapify(freq)
        q = deque()
        t = 0

        while q or freq:
            t += 1
            if freq:
                task = heapq.heappop(freq)
                task += 1
                if task:
                    q.append([task, t+n])

            if q and q[0][1] == t:
                new_task = q.popleft()[0]
                heapq.heappush(freq, new_task)

        return t


#I tried this approach but it will not work
class Solution:
    def leastInterval(self, tasks, n):
        count = {}
        for t in tasks:
            if t in count:
                count[t] += 1
            else:
                count[t] = 1

        time_map = {}
        task_map = []
        for t in count:
            heapq.heappush(task_map, (-count[t], t))

        res = []
        time = 0
        while task_map:
            c1,t1 = heapq.heappop(task_map)
            time += 1
            if t1 in time_map and time - time_map[t1] < n:
                c2, t2 = heapq.heappop(task_map)
                res.append(t2)
                if c2+1:
                    heapq.heappush(task_map, (c2+1, t2))
                    time_map[t2] = time

            else:
                res.append(t1)
                time_map[t1] = time
                c1 += 1

            if c1:
                heapq.heappush(task_map, (c1,t1))

        return ''.join(res)


#this solution is working
#revised on 16-10-2023
class Solution:
    def leastInterval(self, tasks, n):
        count = {}
        for t in tasks:
            if t in count:
                count[t] += 1
            else:
                coutn[t] = 1

        freq = []
        for key in count:
            heapq.heappush(freq, -count[key])

        q = deque()
        t = 0

        while q or freq:
            t += 1
            if freq:
                task = heapq.heappop(freq)
                if task+1:
                    q.append([task+1, t+n])

            if q and q[0][1] = t:
                task, time = q.popleft()
                heapq.heappush(task)

        return t
