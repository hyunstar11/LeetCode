# Binary Serach Example 

class Solution:
    def mySqrt(self, n: int) -> int:

        # check if the given number is negative ; 음수면 sqrt 를 구할 수 가 없음 
        if n < 0 : 
            return False 
        # 0 이나 1인 경우에는 sqrt 가 정해져 있음. 
        if n == 0 or n == 1:
            return n
        
        # initialize two vars: 'start' and 'end'
        start = 0
        end = n
        sqrt = 0

        while start <= end:
            mid = (start + end) // 2

            if mid * mid == n:
                return mid
            elif mid * mid < n:
                # 가장 작은 integer 인 1 단위로 업데이트.. 밑에도 동일함
                start = mid + 1
                sqrt = mid
            else:
                end = mid - 1

        return sqrt
        
#         if n < 0:
#             return "Invalid input. Please enter a non-negative number."
#         if n == 0 or n == 1:
#             return n



