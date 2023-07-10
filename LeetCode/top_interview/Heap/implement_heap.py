class heap:
    def __init__(self):
        self.heap = []
    
    def heappush(self, val):
        self.heap.append(val)
        self.heap_up(len(self.heap)-1)

    def heappop(self):
        if self.heap:
            self.swap(0, len(self.heap)-1)
            smallest = self.heap.pop()
            self.heap_down(0)
            return smallest

    def swap(self, id1, id2):
        self.heap[id1], self.heap[id2] = self.heap[id2], self.heap[id1]

    def heap_up(self, curr):
        while curr > 0 and self.heap[(curr - 1) // 2] > self.heap[curr]:
            self.swap(curr, (curr-1)//2)
            curr = (curr-1) // 2

    def heap_down(self, curr):
        left_child = 2*curr + 1
        right_child = 2*curr + 2
        small = curr

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[curr]: #first check with left child
            small = left_child
        
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[small]: # then check the smaller with right child
            small = right_child

        if small != curr:
            self.swap(curr, small)
            self.heap_down(small)

    def heapify(self, arr):
        self.heap = arr
        n = len(arr)
        start = (n // 2) - 1
        for i in range(start, -1, -1):
            self.heap_down(i)

arr = [7,5,1, 2,3, 9,10]
h = heap()
h.heapify(arr)
print(h.heap)
print(h.heappop())
print(h.heappop())
h.heappush(0.5)
print(h.heap)
print(h.heappop())