class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = [0]*len(spells)

        potions = sorted(potions)
        n = len(potions)

        for i in range(len(spells)):
            
            low = 0
            high = n - 1

            while low <= high:
                mid = (low + high)//2

                if potions[mid]*spells[i] >= success:
                    high = mid - 1
                else:
                    low = mid + 1
            
            pairs[i] = n - low 
            
        return pairs


            
        