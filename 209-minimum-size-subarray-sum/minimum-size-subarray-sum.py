class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        check = 0
        length = 10000000

        for r in range(len(nums)):
            check += nums[r]

            while check >= target:
                length = min(length, r - l + 1)
                check -= nums[l]
                l+=1

        if length > len(nums):
            return 0

        return length
