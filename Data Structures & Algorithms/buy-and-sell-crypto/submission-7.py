class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxP = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxP = max(profit, maxP)
                sell += 1
            else:
                buy = sell
                sell += 1
        
        return maxP