class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for i in range(len(nums)):
            seq = 1
            val = nums[i]
            if val - 1 in numSet:
                continue
            while val + 1 in numSet:
                seq += 1
                val += 1
            res = max(res, seq)
        
        return res

