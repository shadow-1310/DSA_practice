# this is a wrong solution. kept it for future refrence
def merge(intervals):
    first = 0
    while first < len(intervals):
        second = first + 1
        while second < len(intervals):
            if intervals[first][0] <= intervals[second][0]:
                if intervals[second][0] <= intervals[first][-1]:
                    intervals[first][-1] = max(intervals[second][-1], intervals[first][-1])
                    del intervals[second]

                else:
                    second += 1

            else:
                if intervals[first][0] <= intervals[second][-1]:
                    intervals[first][0] = intervals[second][0]
                    intervals[first][-1] = max(intervals[second][-1], intervals[first][-1])
                    del intervals[second]

                else:
                    second += 1
                    
        first += 1

    return intervals


# this is correct solution. done on 02-06-2023
# idea is to sort the array based on first element. then iterate and apply condition for overlap
def merge(intervals):
    intervals.sort(key = lambda x:x[0])
    output = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = output[-1][1]

        if start <= last_end:
            output[-1][1] = max(end, last_end)

        else:
            output.append([start, end])
    
    return output


intervals1 = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[1,4],[4,5]]
intervals3 = [[1,4], [0, 4]]
intervals4 = [[1,4],[2,3]]

print(merge(intervals1))
print(merge(intervals2))
print(merge(intervals3))
print(merge(intervals4))