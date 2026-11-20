class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preMap = {0 : 1}
        sum = 0
        res = 0

        for num in nums:
            sum += num
            if sum - k in preMap:
                res += preMap[sum - k]
            preMap[sum] = preMap.get(sum, 0) + 1
        
        return res
            