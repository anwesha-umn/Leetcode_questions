class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #method 1
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
 
        return k

        #method 2
        # set_nums = sorted(list(set(nums)))
        
        # for i in range(len(set_nums)):
        #     nums[i]=set_nums[i]
        
        # return len(set_nums)
        