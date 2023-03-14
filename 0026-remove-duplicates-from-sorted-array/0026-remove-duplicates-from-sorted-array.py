class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: # input 이 빈 상태라면 
            return 0 # 제대로 평가할 수 없으니 0을 반환.. 

        i = 0  # pointer to keep track of the current unique element ; 포인터 initialize 
        for j in range(1, len(nums)): # 두 번째 포인터 
            if nums[j] != nums[i]:  # if the next element is not a duplicate
                i += 1 # 서로 다른 unique한 숫자니까 + 1 
                nums[i] = nums[j]  # move the unique element pointer and copy the element ; 그 유니크한 숫자를 i 로 설정해준다. 

        return i + 1  # return the number of unique elements ; i는 0부터 시작했기 때문에 