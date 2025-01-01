# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # firs sort the list
        nums.sort()

        # set closest sum to inf
        closest_sum = 10**10

        # 3 pointer approach, we need to return closest sum
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while (j < k):
                current_sum = nums[i] + nums[j] + nums[k]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum > target:
                    k -= 1
                elif current_sum < target:
                    j += 1
                else:
                    # if current_sum = target
                    return current_sum

        return closest_sum
