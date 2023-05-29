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


piles = [3,6,7,11]
h = 8

piles2 = [30,11,23,4,20]
h2 = 5

piles3 = [30,11,23,4,20]
h3 = 6

print(find_rate(piles, h))
print(find_rate(piles2, h2))
print(find_rate(piles3, h3))