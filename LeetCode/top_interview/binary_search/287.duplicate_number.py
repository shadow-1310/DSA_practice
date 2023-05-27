# this approach uses extra space of N in form of the dict
# the other approach implementing linked list cycle is not intuitive
def find_duplicate(nums):
    count_freq = {}

    for num in nums:
        if num not in count_freq:
            count_freq[num] = 1
        else:
            return num
        

nums = [1,3,4,2,2]

print(find_duplicate(nums))