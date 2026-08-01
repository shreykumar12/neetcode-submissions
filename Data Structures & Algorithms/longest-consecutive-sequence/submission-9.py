class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in range(len(nums)):
            val = nums[i]
            seq = 1
            if val - 1 in numSet:
                continue
            while val + 1 in numSet:
                seq += 1
                val += 1
            res = max(seq, res)
        
        return res