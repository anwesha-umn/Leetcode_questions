class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = 0
        zeros = 0
        length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            if zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            length = max(length, right - left)

        return length

        

