class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            print(diff)
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i
            print(seen)
        return []