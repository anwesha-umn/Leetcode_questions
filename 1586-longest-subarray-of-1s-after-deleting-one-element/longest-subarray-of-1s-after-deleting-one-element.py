class Solution:
    def longestSubarray(self, nums: List[int]) -> int:


        l=0
        zeros = 0
        count = 0
        for r in range(len(nums)):
            if nums[r]==0:
                zeros+=1

            if zeros > 1:
                if nums[l]==0:
                    zeros-=1
                l += 1

            count = max(count,r-l)

        return count
        