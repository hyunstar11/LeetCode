class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maximum = 0 
        lowprice = 99999
        for price in prices: 
            if price < lowprice: 
                lowprice = price 
            elif price - lowprice > maximum: 
                maximum = price - lowprice 
        return maximum