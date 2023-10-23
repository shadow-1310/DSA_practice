#first done on 23-10-2023
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms):
        q = deque()
        visited = set()
        q.append(0)

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                for nei in rooms[curr]:
                    q.append(nei)

        return len(visited) == len(rooms)


rooms1 = [[1],[2],[3],[]]
rooms2 = [[1,3],[3,0,1],[2],[0]]
s = Solution()
print(s.canVisitAllRooms(rooms1))
print(s.canVisitAllRooms(rooms2))
