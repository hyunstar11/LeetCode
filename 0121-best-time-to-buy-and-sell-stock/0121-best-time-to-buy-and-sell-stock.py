class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 9999999
        max_profit = 0 
        
        for price in prices: 
            if price < min_price: 
                min_price = price
                #profit = prices[p] - min_price
            elif price - min_price > max_profit:
                max_profit = price - min_price 
        return max_profit 
        
# my original logic(틀렸을수도 ㅠ)        
# thinking about the basic logic here 
# 1. an array is given 
# 2. find the min and max prices in the array 
# 3-1. compare the index of the min and max prices 
# 3-2. if the index of the min > max price, search the next max in the array.. 
# 3-3. if there is none or if the index of the minimum number is the last digit, then return 0 
# 4. if there is a next max, then the output should be max - minimum. 

    