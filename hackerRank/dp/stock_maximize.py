def stockmax(prices):
    profit = 0
    max_price = prices[-1]

    for i in range(len(prices)-2, -1, -1):
        if prices[i] >= max_price:
            max_price = prices[i]

        else:
            profit += max_price - prices[i]

    return profit
