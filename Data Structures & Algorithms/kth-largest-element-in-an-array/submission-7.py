class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        num = 0
        while k > 0:
            num = heapq.heappop_max(nums)
            k -= 1
        
        return num