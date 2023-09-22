def rotated_sorted_array(nums, target):
    '''
    this approach is not working properly for all test cases. But I have kept it here to remind me of my mistake
    '''
    l = 0
    r = len(nums)-1
    while l <= r:
        mid = l + ((r-l)//2)
        if target < nums[mid]:
            if target < nums[l]:
                l = mid + 1
            elif target > nums[l]:
                r = mid-1
            else:
                return mid
        
        elif target > nums[mid]:
            if target < nums[r]:
                l = mid+1
            elif target > nums[r]:
                l = mid+1
            else:
                return mid
        
        else:
            return mid
    
    return -1


def rotated_array(nums, target):
    '''
    this is the correct solution
    '''
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2

        #checking if target is the middle element
        if target == nums[mid]:
            return mid
        
        #it will execute if midpoint is in left segment
        if nums[mid] > nums[right]:
            if target > nums[mid] or target < nums[left]:
                left = mid+1
            else:
                right = mid-1
        #when midpoint is in right segment
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid-1
            else:
                left = mid+1

    return -1

#this is a revision done on 2023-09-22
class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        mid = (left+right) // 2
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[right]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1

                else:
                    right = mid - 1

            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1

                else:
                    left = mid + 1

        return -1





nums = [4,5,6,7,0,1,2]
target = 0

nums2 = [1]
target2 = 0

nums3 = [4,5,6,7,0,1,2, 3]
target3 = 3

print(rotated_array(nums, target))
print(rotated_array(nums2, target2))
print(rotated_array(nums3, target3))
