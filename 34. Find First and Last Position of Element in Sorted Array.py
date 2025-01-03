"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def get_index(first, nums, target):
            
            l = 0
            r = len(nums) - 1 
            result = -1

            while(l <= r):
                mid = l + (r - l)//2

                if nums[mid] == target:
                    result = mid

                    if first:
                        r = mid - 1
                    else:
                        l = mid + 1
                
                elif nums[mid] > target:
                    r = mid - 1
                
                else:
                    l = mid + 1

            return result

        first = get_index(True,nums,target)
        last = get_index(False,nums,target)

        return [first, last]
