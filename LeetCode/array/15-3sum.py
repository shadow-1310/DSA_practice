def three_sum(arr: list[int]) -> list[int]:
    arr.sort()
    result = []
    n = len(arr) - 1
    for i in range(n):
        l = i + 1
        r = n
        if i > 0 and arr[i] == arr[i-1]:  # removes duplicate entry
            continue
        while l < r:
            sum = arr[i] + arr[l] + arr[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                result.append([arr[i], arr[l], arr[r]])
                l += 1  # put this line before the while loop
                while arr[l] == arr[l-1] and l < r:  # this removes duplicate entry
                    l += 1

    return result


class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1

                else:
                    right -= 1


        return res

                


nums = [0, 0, 0]
print(three_sum(nums))
print(len(nums))
