class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)

        freq = {}

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1

        for item, val in freq.items():
            if freq[item] > n/2:
                return item

        
        