class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # get the start index number in rotated array
        n = len(nums)
        
        # if k is > len(nums)
        k = k % n      
        rotated = [0] * n

        for i in range(n):
            rotated[(i + k) % n] = nums[i]

        for i in range(n):
            nums[i] = rotated[i]

       