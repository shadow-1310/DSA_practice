# this is first attempt on 01-06-2023
def find_longest(nums):
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)
    check_list = set(nums)
    max_count = 0
    for num in nums:
        if num - 1 not in check_list:
            count = 1
            while True:
                if num + 1 in check_list:
                    count += 1 
                    max_count = max(count, max_count)
                    num += 1
                else:
                    break

    return max(max_count, count)


nums1 = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
nums3 = [0]
nums4 = []

print(find_longest(nums1))
print(find_longest(nums2))
print(find_longest(nums3))
print(find_longest(nums4))