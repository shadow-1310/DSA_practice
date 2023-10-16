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


class Solution:
    def findKthLargest(self, nums, k):
        nums = [-n for n in nums]
        count = 0
        heapq.heapify(nums)
        while nums:
            curr = heapq.heappop(nums)
            count += 1
            if count == k:
                return -curr

nums = [3,2,1,5,6,4]; k = 2
nums2 = [3,2,3,1,2,4,5,5,6]; k2 = 4
s = Solution()
print(s.findKthLargest(nums, k))
print(s.findKthLargest(nums2, k2))
