class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        minSub = len(nums) + 1
        
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minSub = min(minSub, r-l+1)
                total -= nums[l]
                l += 1
        
        if minSub == len(nums) + 1:
            return 0
        return minSub
