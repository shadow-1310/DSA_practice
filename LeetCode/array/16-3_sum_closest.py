# done on 13-09-2025, passed all test cases on first attempt
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float("inf")
        for i, num1 in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = num1 + nums[left] + nums[right]
                if total == target:
                    return total
                elif total < target:
                    if abs(total-target) < abs(res - target):
                        res = total
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                else:
                    if abs(total-target) < abs(res - target):
                        res = total
                    right -= 1

        return res
