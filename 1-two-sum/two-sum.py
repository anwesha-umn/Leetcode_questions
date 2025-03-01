class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # use nums[i] and complement of nums[i]
        nums_dict = {}

        for i in range(len(nums)):
            nums_dict[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_dict and nums_dict[complement]!=i:
                return [i,nums_dict[complement]]
