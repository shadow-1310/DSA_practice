from typing import List
import heapq

#this is a correct solution using min heap approach
# done on 07-07-2023
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums] # this is a mistake, no need to implement max heap, min heap of size k will give kth largest
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        
        return -nums[0]