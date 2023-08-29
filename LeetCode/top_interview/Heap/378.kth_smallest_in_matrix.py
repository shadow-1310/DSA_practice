import heapq
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        rows = min(k, m)
        min_heap = [(row[0], i, 0) for i, row in enumerate(matrix[:rows])]
        heapq.heapify(min_heap)

        ans = None

        for i in range(k):
            ans, r, c = heapq.heappop(min_heap)
            if c+1 < n:
                heapq.heappush(min_heap, (matrix[r][c+1], r, c+1))

        return ans

# this is a revision, correct solution done on 29-08-2023 
class Solution:
    def kthSmallest(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])

        rows = min(k, m)
        min_heap = []
        for i, row in enumerate(matrix[:rows]):
            heapq.heappush(min_heap, (row[0], i, 0))

        for i in range(k):
            ans, r, c = heapq.heappop(min_heap)
            if c+1 < n:
                heapq.heappush(min_heap, (matrix[r][c+1], r, c+1))

        return ans

