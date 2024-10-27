class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0 
        lowestprice = 999999 
        for price in prices: 
            if price < lowestprice: 
                lowestprice = price 
            elif price - lowestprice > maxprofit: 
                maxprofit = price - lowestprice 
        return maxprofit 