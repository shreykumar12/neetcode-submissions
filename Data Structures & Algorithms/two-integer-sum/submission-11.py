class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in vals:
                return [vals[diff], i]
            vals[nums[i]] = i
        return []