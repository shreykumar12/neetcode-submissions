class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        i = 0

        while i < len(nums) and k > 1:
            i += 1
            k -= 1
        
        return nums[i]