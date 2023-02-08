class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxi = 0 
        
        for i in nums: 
            if i == 0: 
                count = 0
            else: 
                count = count + 1 
                maxi = max(count,maxi)
        return maxi