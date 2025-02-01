class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        exp = set([i+1 for i in range(len(nums))])
        set_nums = set(nums)
        
        return list(exp - set_nums)

        



