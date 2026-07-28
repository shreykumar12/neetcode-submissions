class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0

        i = 0
        while i < len(nums):
            ones = 0
            while i < len(nums) and nums[i] == 1:
                ones += 1
                i += 1
            total = max(total, ones)
            i += 1
        
        return total
