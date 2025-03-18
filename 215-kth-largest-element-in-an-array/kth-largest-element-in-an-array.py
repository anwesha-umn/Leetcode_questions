class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # using heapq: If heap has data more than k, just pop data from heap. 
        # In the end, top data in heap should be k largest number.
        
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]


        
