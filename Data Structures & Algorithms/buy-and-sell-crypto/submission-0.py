class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxP = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                if profit > maxP:
                    maxP = profit
                sell += 1
            else:
                buy = sell
                sell += 1
        return maxP
