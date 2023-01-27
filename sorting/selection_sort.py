def sort_selection(arr:list):
    n = len(arr) 
    count = 0    
    for i in range(n):
        min = arr[i]
        min_id = i
        for j in range(i, n):
            if arr[j] < min:
                min = arr[j]
                min_id = j
                count += 1
        arr[i], arr[min_id] = arr[min_id], arr[i]
        
    print("No. of swaps: ",count)

a = [2, 4, 3, 1, 5]
print("before sorting: ",a)
sort_selection(a)
print("After sorting: ", a)
