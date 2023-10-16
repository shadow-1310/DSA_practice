from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while stones and len(stones) > 1:
            heavy1 = (-1)*heapq.heappop(stones)
            heavy2 = (-1)*heapq.heappop(stones)

            new = heavy1 - heavy2

            if new > 0:
                heapq.heappush(stones, -new)

        return -stones[0] if stones else 0
    
class Solution:
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while stones:
            if len(stones) < 2:
                break
            
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            new_stone = stone1 - stone2

            if new_stone == 0:
                continue

            else:
                heapq.heappush(stones, new_stone)

        return -stones[0] if stones else 0

#this revision was done on 16-0-2023
class Solution:
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            if s1 != s2:
                s3 = s1 - s2
                heapq.heappush(stones, s3)

        return -stones[0] if stones else 0


s = Solution()
stones = [2,7,4,1,8,1]
last = s.lastStoneWeight(stones)
print(last)



