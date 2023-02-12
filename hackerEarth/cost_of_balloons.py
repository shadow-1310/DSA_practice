# my method
test_cases = int(input())
test_case = 0
while test_case < test_cases:
    costs = input()
    cost_green = int(costs.split()[0])
    cost_purple = int(costs.split()[1])
    num_participant = int(input())
    first_problem = 0
    second_problem = 0
    for i in range(num_participant):
        solved = input()
        first_problem += int(solved.split()[0])
        second_problem += int(solved.split()[1])
    min_cost = min(first_problem, second_problem) * max(cost_green, cost_purple) + max(first_problem, second_problem) * min(cost_green, cost_purple)
    print(min_cost)
    test_case += 1

# took from youtube/github
test_cases = int(input())
for i in range(test_cases):
    p, g = map(int, input().split())
    low = min(p, g)
    high = max(p, g)
    cost = 0

    p1_total = 0
    p2_total = 0
    n = int(input())
    for j in range(n):
        p1, p2 = map(int, input().split())
        p1_total += p1
        p2_total += p2

    if p1_total > p2_total:
        cost += p1_total * low
        cost += p2_total * high
    else:
        cost += p2_total * low
        cost += p1_total * high
    print(cost)