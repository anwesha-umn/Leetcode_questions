class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort the array
        nums.sort()
        output = []

        
        for i in range(len(nums) - 3): # we have to keep 3 pointers on the right side of i pointer
            # avoid duplicate starting values
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range (i+1, len(nums) - 2): 
                # skip duplicates
                if j > i+1 and nums[j]==nums[j-1]:
                    continue

                l = j + 1
                r = len(nums) -  1

                while l < r:
                    curr = nums[i] + nums[j] + nums[l] + nums[r]
                    if curr == target:
                        s = [nums[i], nums[j], nums[l], nums[r]]
                        output.append(s)
                        
                        l += 1
                        r -= 1

                        # Skip duplicates
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1

                    elif curr < target:
                        l += 1

                    else:
                        r -= 1

                
        return output


        