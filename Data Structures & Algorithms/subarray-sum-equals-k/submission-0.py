class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = { 0 : 1}
        sum = 0
        res = 0

        for num in nums:
            sum += num
            diff = sum - k
            
            res += map.get(diff, 0)
            map[sum] = map.get(sum, 0) + 1
        
        return res
        