#done on 11-11-2023
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        n = len(heights)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height*(i-index))
                start = index
            stack.append([start, h])

        for i,h in stack:
            max_area = max(max_area, h*(n-i))

        return max_area


