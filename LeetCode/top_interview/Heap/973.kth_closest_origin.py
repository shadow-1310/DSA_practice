from typing import List
import heapq
from math import sqrt

#this is a wrong solution as it implemented max-heap, we need to implement min heap and return whenever len(res) == k
#done on 07-07-2023
class Solution:
    def kClosest_wrong(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = {}
        res = []
        for point in points:
            x = point[0]
            y = point[1]
            # dist = round(sqrt(x**2 + y**2),3)
            dist = x**2 + y**2
            if dist not in dic:
                dic[dist] = [point]
            else:
                dic[dist].append(point)
        
        dist = [-key for key in dic]
        heapq.heapify(dist)
        while len(dist) > k:
            heapq.heappop(dist)

        while dist:
            point = dic[-heapq.heappop(dist)]
            for p in point:
                res.append(p)
                if len(res) == k:
                    return res

# this is correct solution using min heap of all elements
# done on 07-07-2023    
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = {}
        res = []
        for point in points:
            x = point[0]
            y = point[1]
            # dist = round(sqrt(x**2 + y**2),3)
            dist = x**2 + y**2
            if dist not in dic:
                dic[dist] = [point]
            else:
                dic[dist].append(point)
        
        dist = [key for key in dic]
        heapq.heapify(dist)
 
        while dist:
            point = dic[heapq.heappop(dist)]
            for p in point:
                res.append(p)
                if len(res) == k:
                    return res

# this is a revision with the shortest best solution
# done on 06-08-2023

class Solution:
    def kClosest(self, points, k):
        res = []

        for i in range(len(points)):
            x, y = points[i]
            dist = x**2 + y**2
            points[i] = (dist, [x,y])

        heapq.heapify(points)

        while points:
            node = heapq.heappop(points)
            res.append(node[1])
            if len(res) == k:
                break

        return res


points1 = [[1,3],[-2,2]]
k1 = 1

points2 = [[3,3],[5,-1],[-2,4]]
k2 = 2

points3 = [[1,3],[-2,2],[2,-2]]
k3 = 2
s = Solution()
print(s.kClosest(points3, k3))
