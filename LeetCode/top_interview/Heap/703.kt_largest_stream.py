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


#although it is correct approach it will take more time, no need to maintain this big heap, instead maintain a heap of size k
class KthLargest:
    def __init__(self, k, nums):
        self.nums = [-n for n in nums]
        self.cap = k
        heapq.heapify(self.nums)
        
    def add(self, val):
        heapq.heappush(self.nums, -val)
        temp = []
        count = 0
        while self.nums:
            temp.append(heapq.heappop(self.nums))
            count += 1
            if count == self.cap:
                break
        for n in temp:
            heapq.heappush(self.nums, n)

        return -temp[-1]


class Solution:
    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
