class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # sorted array duplicates - means they should be adjacent to each other 

        # create a new start index k - for non-repeating elememts
        if len(nums) <=1:
            return len(nums)
        k = 0
        i = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[k] = nums[i]
                k+=1
        nums[k] = nums[i+1]
        
        return k+1

         
