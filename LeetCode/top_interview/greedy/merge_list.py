import heapq

#this question was asked in AMEX campus OA, it is based optimum merge pattern of Greedy
def find_min_time(lists):
    heapq.heapify(lists)
    time = 0
    while len(lists) > 1:
        list1 = heapq.heappop(lists)
        list2 = heapq.heappop(lists)
        time += list1 + list2
        heapq.heappush(lists,time)
    
    return lists[0]

l = [100,250,1000]
print(find_min_time(l))
