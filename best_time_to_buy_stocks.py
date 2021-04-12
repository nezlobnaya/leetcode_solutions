class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        
        N =len(prices)
        min_price = prices[0]
        max_profit = prices[1]-prices[0]
        
        for i in range(1,N):
            temp=prices[i]
            potential_profit = temp - min_price
            max_profit = max(max_profit, potential_profit)
            min_price = min(min_price,temp)
            
        return 0 if max_profit< 0 else max_profit