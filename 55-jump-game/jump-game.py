class Solution:
    def canJump(self, nums: List[int]) -> bool:
            
        jump = 0
        for n in nums:
            if jump < 0:     # first check if jump < 0 -- means no jump, return false
                return False

            if n > jump:
                jump = n
            
            jump -= 1  # cross each step and reduce jump by 1
            
        return True
