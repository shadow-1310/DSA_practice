# def remove_duplicates(nums):
#     count = {}
#     for position, num in enumerate(nums):
#         if num not in count:
#             count[num] = 1
#         else:
#             nums.pop(position)
#     return len(list(count.keys()))


def remove_duplicates(nums):
    i = 0
    while i < len(nums):
        if i != 0 and nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


#this is a revision done on 10-09-2023, woekin well on LC testcases
#it is different from previous by the fact that it also stores duplicated value in the end as '_'
class Solution:
    def removeDuplicates(self, nums):
        tot = len(nums)
        duplicates = 0
        i = 0

        while i < tot and nums[i] != '_':
            if i > 0 and nums[i] == nums[i-1]:
                nums.pop(i)
                nums.append('_')
                duplicates += 1

            else:
                i += 1

        return tot - duplicates

nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(nums))
