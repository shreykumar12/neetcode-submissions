class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = {0:1}
        res = 0
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            diff = sum - k

            res += prefixMap.get(diff, 0)
            prefixMap[sum] = prefixMap.get(sum, 0) + 1
        
        return res