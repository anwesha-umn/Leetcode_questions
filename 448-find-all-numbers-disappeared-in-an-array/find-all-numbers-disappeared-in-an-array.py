class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        expected = [i+1 for i in range(len(nums))]
        nums_set = set(nums)

        return list(set(expected) - set(nums_set))

