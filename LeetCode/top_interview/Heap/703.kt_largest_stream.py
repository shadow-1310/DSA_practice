from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

#it is done on 29-08-2023 and correct solution
class KthLargest:
    def __init__(self, k, nums):
        self.h = nums
        heapq.heapify(self.h)
        self.k = k

    def add(self, val):
        heapq.heappush(self.h, val)

        while len(self.h) > self.k:
            heapq.heappop(self.h)

        return self.h[0]
