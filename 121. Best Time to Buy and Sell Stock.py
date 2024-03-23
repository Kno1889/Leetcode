class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]

            elif max_profit < prices[i] - lowest:
                max_profit = prices[i] - lowest
        
        return max(max_profit, 0)
        