class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math 
        
        def feasible(count):
            speed = [math.ceil(pile/count) for pile in piles]
            if sum(speed) <= h:
                return True
            else:
                return False
        
        low = 1
        high = max(piles)

        while low <= high:

            mid = (low + high)//2

            if feasible(mid):
                # we need least value of k
                high = mid - 1
            else:
                low = mid + 1

        
        return low  # count of bananas per hour
