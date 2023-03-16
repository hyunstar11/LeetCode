class Solution:
    def isPalindrome(self, x: int) -> bool:
#         # reverse the integer ? how? 
#         reversed_num = 0 
#         is_neg = False 
        
#         # Is negative? 
        
#         if n < 0: 
#             return False 
        
#         if n == 10:
#             return False 
        
#         if n == 100:
#             return False 
        
#         if n == 0: 
#             return True 
            
#         # string을 사용하지 않고 리버스하기 
        
#         while n > 0: 
#             remainder = n % 10 
#             reversed_num = reversed_num * 10 + remainder 
#             n = n // 10 
            
#         return -reversed_num if is_neg else reversed_num 
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:
            remainder = x % 10
            reversed_num = reversed_num * 10 + remainder
            x = x // 10

        return original == reversed_num


