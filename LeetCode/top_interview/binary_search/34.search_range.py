#original implementation, too lengthy and not working for the edge case where target element is in the right/left point position
def find_position(nums, target):
    left = 0
    right = len(nums)-1
    target_index = 0
    flag = False

    while left <= right:
        mid = (left+right) // 2
        
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid-1
        else:
            target_index = mid
            flag = True
            break

    left = 0
    right = target_index-1
    first = target_index

    while left <= right:
        mid = (left+right) // 2
        
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid-1
        else:
            first = mid
            break

    left = target_index + 1
    right = len(nums)-1
    last = target_index

    while left <= right:
        mid = (left+right) // 2
        
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid-1
        else:
            last = mid
            break

    if flag:
        return [first, last]
    else:
        return [-1,-1]


# this is the correct function
# def find_range(nums, target):
#     #making a helper function which will iteratively bi_search left or right interval depending on the parameter "bias"
#     def bi_search(nums, target, bias):
#         left = 0
#         right = len(nums)-1
#         index = -1
#         while left <= right:
#             mid = (left+right) // 2

#             if target > nums[mid]:
#                 left = mid+1
#             elif target < nums[mid]:
#                 right = mid-1
#             else:
#                 index = mid
#                 # extensively serach in the left interval
#                 if bias == 'left':
#                     right = mid-1
#                 #extensively bi_search in the right interval
#                 elif bias == 'right':
#                     left = mid+1

#         return index
        

#     left_position = bi_search(nums, target, bias='left')
#     right_position = bi_search(nums, target, bias='right')
    
#     return [left_position, right_position]


# this is a revision. done on 11-06-23.
#mistake I was doing is calculating value of mid outside the while loop
def find_range(nums, target):
    def bi_search(nums, target, right = True):
        l = 0
        r = len(nums)-1
        index = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            
            elif nums[mid] < target:
                l = mid + 1

            else:
                index = mid

                if right:
                    l = mid + 1

                else:
                    r = mid - 1

        return index
    

    first = bi_search(nums, target, right=False)
    last = bi_search(nums, target, right=True)

    return [first, last]

#iit was done on 2023-09-22
#this is a very wrong approach and 
class Solution:
    def searchRange(self, nums, target):
        #it is a helper function
        def search_dir(l, r, right:bool):
            if right:
                while l <= r:
                    m = (l+r) // 2
                    if nums[m] == target:
                        return m
                    if m + 1 < len(nums) and nums[m] == nums[m+1] == target:
                        if m+1 == len(nums)-1:
                            return m+1
                        return search_dir(l = m+1, r, right=True)
                    else:
                        return search_dir(l, r = m-1, right =True)

            else:
                while l <= r:
                    m = (l+r) // 2
                    if nums[m] == target:
                        return m
                    if m - 1 > 0 and nums[m] == nums[m-1] == target:
                        if m-1 == 0:
                            return m-1
                        return search_dir(l, r=m-1, right=False)
                    else:
                        return search_dir(l = m+1, r, right =False)


        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                left_lim = search_dir(0, mid-1, right=False)
                right_lim = search_dir(mid+1, len(nums)-1, right=True)
                return  [left_lim, right_lim]
            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1
        
        return [-1,-1]


class Solution:
    def searchRange(self, nums, target):
        def search_dir(right = True):
            res = -1
            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = (l+r) // 2
                if nums[mid] < target:
                    r = mid - 1

                elif nums[mid] > target:
                    l = mid + 1

                else:
                    res = mid
                    if right:
                        l = mid + 1

                    else:
                        r = mid - 1

            return res

        left_lim = search_dir(right = False)
        right_lim = search_dir(right= True)

        return [left_lim, right_lim]

nums = [5,7,7,8,8,8]
target = 8

nums2 = []
target2 = 1

print(find_range(nums, target))
# print(find_range(nums2, target2))
