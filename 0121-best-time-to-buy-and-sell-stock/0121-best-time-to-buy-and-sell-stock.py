class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = 99999999 ### had issue here 
        max_profit = 0       ### had issue here 
        
        for price in prices: 
            if price < min_price: 
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit