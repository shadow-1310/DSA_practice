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
def find_range(nums, target):
    #making a helper function which will iteratively search left or right interval depending on the parameter "bias"
    def bi_search(nums, target, bias):
        left = 0
        right = len(nums)-1
        index = -1
        while left <= right:
            mid = (left+right) // 2

            if target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
            else:
                index = mid
                # extensively serach in the left interval
                if bias == 'left':
                    right = mid-1
                #extensively search in the right interval
                elif bias == 'right':
                    left = mid+1

        return index
        

    left_position = bi_search(nums, target, bias='left')
    right_position = bi_search(nums, target, bias='right')
    
    return [left_position, right_position]

nums = [5,7,7,8,8,8]
target = 8

nums2 = []
target2 = 1

print(find_range(nums, target))
print(find_range(nums2, target2))