class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = { 0 : 1}
        sum = 0
        count = 0

        for num in nums:
            sum += num
            diff = sum - k

            count += prefixMap.get(diff, 0)
            prefixMap[sum] = prefixMap.get(sum, 0) + 1
        
        return count
            
