def main():
    tcs = int(input())
    for _ in range(tcs):
        n, days = map(int, input().split())
        cities = [0] * n

        for i in range(days):
            start, end = map(int, input().split())
            start = start - 1
            count = 1
            
            for j in range(start, end):
                cities[j] += count
                count += 1

        print(*cities)

# print(*[1,2,3])
# main()
