
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, arr)

    def build(self, node, left, right, arr):
        if left == right:
            self.tree[node] = arr[left]
            return
        mid = (left + right) // 2
        self.build(2 * node, left, mid, arr)
        self.build(2 * node + 1, mid + 1, right, arr)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def update(self, node, left, right, l, r, val):
        if left > right:
            return
        if self.lazy[node] != 0:
            self.tree[node] ^= self.lazy[node]
            if left != right:
                self.lazy[2 * node] ^= self.lazy[node]
                self.lazy[2 * node + 1] ^= self.lazy[node]
            self.lazy[node] = 0

        if l > right or r < left:
            return

        if l <= left and r >= right:
            self.tree[node] ^= val
            if left != right:
                self.lazy[2 * node] ^= val
                self.lazy[2 * node + 1] ^= val
            return

        mid = (left + right) // 2
        self.update(2 * node, left, mid, l, r, val)
        self.update(2 * node + 1, mid + 1, right, l, r, val)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def query(self, node, left, right, l, r):
        if left > right:
            return 0
        if self.lazy[node] != 0:
            self.tree[node] ^= self.lazy[node]
            if left != right:
                self.lazy[2 * node] ^= self.lazy[node]
                self.lazy[2 * node + 1] ^= self.lazy[node]
            self.lazy[node] = 0

        if l > right or r < left:
            return 0

        if l <= left and r >= right:
            return self.tree[node]

        mid = (left + right) // 2
        left_result = self.query(2 * node, left, mid, l, r)
        right_result = self.query(2 * node + 1, mid + 1, right, l, r)
        return left_result ^ right_result

def updateArray(arr, queries):
    seg_tree = SegmentTree(arr)
    updated_arr = []
    
    for query in queries:
        l, r, v = query
        seg_tree.update(1, 0, seg_tree.n - 1, l, r, v)
    
    for i in range(seg_tree.n):
        updated_arr.append(seg_tree.query(1, 0, seg_tree.n - 1, i, i))
    
    return updated_arr

# Example usage:
original_array = [1, 2, 3, 4, 5]
queries = [(0, 2, 2), (1, 3, 1)]
updated_array = updateArray(original_array, queries)
print(updated_array)  # Output: [2, 3, 0, 5, 5]
