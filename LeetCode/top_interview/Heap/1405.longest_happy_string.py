from typing import List
import heapq

#this is a correct solution done using max-heap approach
# done on 10-07-2023
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        max_heap = []
        input_char = [(-a, "a"), (-b, "b"), (-c, "c")]
        for count, char in input_char:
            if count:
                heapq.heappush(max_heap, (count, char))
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not max_heap:
                    break
                
                count2, char2 = heapq.heappop(max_heap)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(max_heap, (count2, char2))

            else:
                res += char
                count += 1
            if count:
                heapq.heappush(max_heap, (count, char))

        return res


class Solution:
    def longestDiverseString(self, a, b, c):
        res = ""
        max_heap = []
        input_char = [(-a, "a"), (-b, "b"), (-c, "c")]

        for count, char in input_char:
            if count:
                heapq.heappush(max_heap, (count, char))


        while max_heap:
            count, char = heapq.heappop(max_heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not max_heap:
                    break
                count2, char2 = heapq.heappop(max_heap)
                res += char2
                count2 += 1

                if count2:
                    heapq.heappush(max_heap, (count2, char2))

            else:
                res += char
                count += 1
            if count:
                heapq.heappush(max_heap, (count, char))

        return res


#don't try to heapify as it will add characters having 0 count
#revision done on 15-10-2023
class Solution:
    def longestDiverseString(self, a, b, c):
        res = []
        count = []
        input_char = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        for c,char in input_char:
            if c:
                heapq.heappush(count, (c,char))
        while count:
            c1, char1 = heapq.heappop(count)
            if len(res) > 1 and res[-1] == char1 and res[-2] == char1:
                if not count:
                    break
                c2, char2 = heapq.heappop(count)
                res.append(char2)
                if c2+1:
                    heapq.heappush(count, (c2+1, char2))
            else:
                res.append(char1)
                c1 += 1
            if c1:
                heapq.heappush(count, (c1, char1))

        return ''.join(res)
                

s = Solution()
print(s.longestDiverseString(1,1,7))
print(s.longestDiverseString(7,1,0))
