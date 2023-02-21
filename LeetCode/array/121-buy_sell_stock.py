def max_profit(prices:list[int]):
    last = len(prices)
    max_profit = 0
    buy = 0
    sell = 1
    while buy < sell and sell < last:
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)
        else:
            buy = sell
        sell += 1

    return max_profit
    

def brute(prices):
    max_profit = 0
    n = len(prices)
    for i in range(n):
        for j in range(i, n):
            profit = prices[j] - prices[i]
            max_profit = max(profit, max_profit)
    return max_profit

test = [1,2,4,2,5,7,2,4,9,0,9]
print(brute(test))
print(max_profit(test))
