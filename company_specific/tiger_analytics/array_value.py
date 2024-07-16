def min_value(a, b, k):
    n = len(a)
    def backtrack(index, tot, x, y):
        if tot == k:
            print((x**2)*y)
            return (x**2)*y
        if index >= n:
            return float('inf')

        mini = backtrack(index+1, tot, x, y)
        mini = min(mini, backtrack(index+1, tot+1, max(x, a[index]), y+b[index]))

        return mini

    return backtrack(0, 0, float('-inf'), 0)

A = [3,2,1]
B = [2,3,4]
K = 2
print(min_value(A,B,K))
