class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0  # pointer to keep track of the current unique element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # if the next element is not a duplicate
                i += 1
                nums[i] = nums[j]  # move the unique element pointer and copy the element

        return i + 1  # return the number of unique elements