class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy, sell = 0, 1
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
                sell += 1
            else:
                buy = sell
                sell += 1
        return maxP
