def two_sum2(arr: list[int], target: int) -> list[int]:
    l = 0
    n = len(arr) - 1
    r = n
    while l < r:
        sum = arr[l] + arr[r]
        if sum > target:
            r -= 1
        elif sum < target:
            l += 1
        else:
            return [l+1, r+1]


class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1

            else:
                right -= 1


class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            curr = numbers[left] + numbers[right]
            if curr > target:
                right -= 1
            elif curr < target:
                left += 1
            else:
                return [left+1, right+1]

        return res




nums = [2, 7, 11, 15]
target = 9
print(two_sum2(nums, target))
