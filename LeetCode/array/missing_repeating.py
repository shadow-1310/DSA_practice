#this is a coding ninja problem
#done on 11-10-2023
def findMissingRepeatingNumbers(a: [int]) -> [int]:
    # Write your code here
    seen = set()
    tot = 0
    n = len(a)
    for num in a:
        tot += num
        if num in seen:
            duplicate = num
        seen.add(num)

    curr = tot-duplicate
    actual = n*(n+1) >> 1
    return [duplicate, actual-curr]


nums = [1,2,3,2]
print(findMissingRepeatingNumbers(nums))
