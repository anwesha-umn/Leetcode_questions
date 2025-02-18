class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        r = 0
        curr = 0
        length = 1000000
        for r in range(len(nums)):
            curr += nums[r]
            
            while curr >= target:
                length = min(length, r - l + 1)
                curr -= nums[l]
                print(length)
                l+=1

        if length > len(nums):
            return 0
        return length


        