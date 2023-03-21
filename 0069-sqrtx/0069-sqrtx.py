# Binary Serach Example 

class Solution:
    def mySqrt(self, n: int) -> int:

        if n < 0:
            return "Invalid input. Please enter a non-negative number."
        if n == 0 or n == 1:
            return n

        start = 0
        end = n
        sqrt = 0

        while start <= end:
            mid = (start + end) // 2

            if mid * mid == n:
                return mid
            elif mid * mid < n:
                start = mid + 1
                sqrt = mid
            else:
                end = mid - 1

        return sqrt
#         # check if the given number is negative 
#         if x < 0 : 
#             return False 
        
#         # initialize two vars: 'low' and 'high'
#         low = 0 
#         high = x 
#         sqrt = 0 
        
#         # how to define a precision threshold? 
#         # precision_threshold = 1e-6
        
#         while low <= high:
#             mid = (low + high)/2 
#             sq_mid = mid * mid 
            
#             if mid * mid == x: 
#                 return sq_mid
#             elif mid*mid < x: 
#                 low = mid + 1  
#                 sq_mid = mid
#             else:
#                 end = mid - 1 
#         return sqrt
