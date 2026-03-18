class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize min_price to a very large number
        # and max_profit to 0
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the lowest price we've seen so far
            if price < min_price:
                min_price = price
            
            # Calculate profit if we sold today
            current_profit = price - min_price
            
            # Update the overall maximum profit
            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit