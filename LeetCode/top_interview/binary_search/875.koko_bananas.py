from math import ceil

def find_rate(piles, h):
    max_rate = piles[0]

    for value in piles:
        max_rate = max(max_rate, value)
    
    def count_hour(piles, rate):
        count = 0
        
        for pile in piles:
            count += ceil(pile / rate )

        return count
    
    left = 1
    right = max_rate
    rate = max_rate

    while left <= right:
        mid = (left+right) // 2
        hour = count_hour(piles, mid)
        
        if hour <= h:
            rate = min(rate, mid)
            right = mid - 1

        else:
            left = mid + 1

    return rate


#this is a revision done on 2023-09-23, working on LC testcases
class Solution:
    def minEatingSpeed(self, piles, h):
        max_pile = max(piles)
        left = 1
        right = max_pile
        if h == len(piles):
            return max_pile
        min_rate = max_pile

        while left <= right:
            mid = (left+right) // 2
            req_hour = 0
            for pile in piles:
                req_hour += ceil(pile/mid)

            if req_hour <= h:
                min_rate = min(min_rate, mid)
                right = mid - 1

            else:
                left = mid + 1

        return min_rate




piles = [3,6,7,11]
h = 8

piles2 = [30,11,23,4,20]
h2 = 5

piles3 = [30,11,23,4,20]
h3 = 6

print(find_rate(piles, h))
print(find_rate(piles2, h2))
print(find_rate(piles3, h3))
