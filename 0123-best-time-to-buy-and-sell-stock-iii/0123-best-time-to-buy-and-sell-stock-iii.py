class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # Initialize states
        # buy1: lowest price to buy first stock
        # sell1: max profit after first sale
        # buy2: max money left after buying second stock with sell1 profit
        # sell2: final max profit
        buy1, buy2 = -float('inf'), -float('inf')
        sell1, sell2 = 0, 0
        
        for price in prices:
            # First transaction cycle
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            
            # Second transaction cycle
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
            
        return sell2