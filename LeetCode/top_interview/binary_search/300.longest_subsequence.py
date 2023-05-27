# this is a dp problem so will attempt it later
# following code is half attempt only
def find_lis(nums):
    start = 0
    prev = start
    curr = prev + 1
    max_lis = 0
    count = 1

    if len(nums) == 1:
        return 1

    while prev < curr and curr < len(nums):
        if nums[start] > nums[start+1]:
            start += 1
            prev = curr
            curr = prev + 1
            count = 1
        
        elif nums[curr] > nums[prev]:
            count += 1
            curr += 1
            max_lis = max(max_lis, count)

        elif nums[right] :
            pass
        
        right += 1
        


nums = [10,9,2,5,3,7,101,18]