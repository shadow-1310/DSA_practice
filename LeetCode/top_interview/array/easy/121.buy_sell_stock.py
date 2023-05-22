def buy_sell_stock(prices):
    buy = 0
    sell = 1
    last = len(prices)
    max_profit = 0
    while buy < sell and sell < last:
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            max_profit = max(profit, max_profit)
        else:
            buy = sell
        
        sell += 1

    return max_profit


prices = [7,1,5,3,6,4]
print(buy_sell_stock(prices))