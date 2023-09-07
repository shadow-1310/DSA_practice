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


#this is a revision done 07-09-2023, it working fine on LC test cases
class Solution:
    def maxProfit(self, prices):
        left = 0
        right = left
        max_profit = 0
        while left <= right and right < len(prices):
            if prices[right] < prices[left]:
                left = right

            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
            right += 1

        return max_profit


prices = [7,1,5,3,6,4]
print(buy_sell_stock(prices))
