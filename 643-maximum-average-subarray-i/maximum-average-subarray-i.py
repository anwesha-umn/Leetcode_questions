class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        sum_array = sum(nums[:k])
        max_sum = sum_array
        j = 0
        for i in range(k, len(nums)):
            sum_array = sum_array + nums[i] - nums[j]
            max_sum = max(max_sum, sum_array)
            j+=1

        return max_sum/k

        