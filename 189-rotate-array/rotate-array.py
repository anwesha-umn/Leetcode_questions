class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        new = []
        while i < k:
            temp = nums.pop()
            nums.insert(0,temp)
            i+=1

       