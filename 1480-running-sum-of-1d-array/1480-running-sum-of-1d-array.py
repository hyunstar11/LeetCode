class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Method #1 
        # the easy way is the use the accumulate function here 
        return accumulate(nums)

        # Method #2 
        # Q. How do we do it without using the function though? 

        nums[i] = nums[i]+nums[i-1]
        return nums 

        # for loop을 짜고, range function 을 잘 써야함. 
        for i in range(1, len(nums)): # range 가 1부터 array 의 길이 만큼 반복 
            nums[i] = nums[i] + nums[i-1] # array의 i=1 즉 두 번째 숫자부터 시작한다. 두 번째 숫자는 = 두 번째 숫자 + 첫번째 숫자... 세 번째 숫자 = 세 번째 + 두 번째 so and so forth 
        return nums # array를 반환한다. 