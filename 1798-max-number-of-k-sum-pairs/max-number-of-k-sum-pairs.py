class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        pairs = 0

        while left < right:
            check = nums[left] + nums[right]

            if check == k:
                pairs += 1
                left += 1
                right -= 1
            elif check < k:
                left += 1
            else:
                right -= 1

        return pairs



        