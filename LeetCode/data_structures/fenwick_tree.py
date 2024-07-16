class Fenwick:
    def __init__(self, arr):
        self.tree = [0] + arr
        self.len = len(arr) + 1
        self.construct()

    #find LSB, least significant bit
    def lsb(self, n):
        return (n & -n)

    #construct the fenwick tree, 1-based
    def construct(self):
        for i in range(1, self.len):
            parent = i + self.lsb(i)
            if parent < self.len:
                self.tree[parent] += self.tree[i]

    #increment idx element by +val
    def point_update(self, idx, val):
        parent = idx
        while parent < self.len:
            self.tree[parent] += val
            parent += self.lsb(parent)

    #find sum upto idx
    def prefix_sum(self, idx):
        res = 0
        while idx:
            res += self.tree[idx]
            idx -= self.lsb(idx)

        return res

    #find sum between l and r
    def range_query(self, l, r):
        return (self.prefix_sum(r) - self.prefix_sum(l-1))


array = [1,2,3,4,5]
f = Fenwick(array)
print(f.range_query(2,5))
f.point_update(3, 2)
print(f.range_query(2,5))
