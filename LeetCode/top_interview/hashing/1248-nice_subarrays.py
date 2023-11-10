from collections import defaultdict

#this is done on 10-11-2023
class Solution:
    def numberOfSubarrays(self, nums, k):
        for i, num in enumerate(nums):
            if num & 1:
                nums[i] = 1
            else:
                nums[i] = 0

        res = 0
        count_map = defaultdict(int)
        count_map[0] = 1
        curr = 0

        for num in nums:
            curr += num
            diff = curr - k
            if diff in count_map:
                res += count_map[diff]
            count_map[curr] += 1

        return res


s = Solution()
nums1 = [2,2,2,1,2,2,1,2,2,2]; k1 = 2
nums2 = [2,4,6]; k2=1
print(s.numberOfSubarrays(nums1, k1))
print(s.numberOfSubarrays(nums2, k2))

