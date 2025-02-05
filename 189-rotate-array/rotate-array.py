class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        rotated =[0] * n
      
        for i in range(len(nums)):
            rotated[(k+i) % n] = nums[i]

        for i in range(len(nums)):
            nums[i] = rotated[i]