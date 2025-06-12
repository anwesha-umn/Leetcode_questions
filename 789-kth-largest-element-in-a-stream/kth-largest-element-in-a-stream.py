class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums    
        self.k = k
        self.nums.sort()  # sort once to apply binary search

    def add(self, val: int) -> int:
        index = self.get_index(val)
        self.nums.insert(index, val)
        return self.nums[-self.k]

    def get_index(self, val:int) -> int:
        
        left = 0
        right = len(self.nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if self.nums[mid] == val:
                return mid
            elif self.nums[mid] > val:
                right = mid - 1
            else:
                left = mid + 1

        return left



   
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)