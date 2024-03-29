def brute(height):
    '''
    this is the brute force approach which will have time complexity of O(n^2)
    '''
    max_area = 0
    for i in range(len(height)):
        for j in range(1, len(height)):
            width = j - i
            length = min(height[i], height[j])
            area = int(width*length)
            max_area = max(area, max_area)
    
    return max_area


def optimize_max_water(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        l = right - left
        h = min(height[left], height[right])
        area = int(l*h)
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area 


#this is a revision done on 04-09-2023, correct solution
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            base = right - left
            h = min(height[left], height[right])
            max_water = max(max_water, base*h)

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1

        return max_water


#revision done 08-10-2023
class Solution:
    def maxArea(self, height):
        max_cap = 0
        left = 0
        right = len(height)

        while left <= right:
            max_cap = max(max_cap, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left += 1

            else:
                right -= 1

        return max_cap

height = [1,8,6,2,5,4,8,3,7]
print(optimize_max_water(height)) 
