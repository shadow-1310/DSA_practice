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
    

s = Solution()
stones = [2,7,4,1,8,1]
last = s.lastStoneWeight([2,7,4,1,8,1])
print(last)