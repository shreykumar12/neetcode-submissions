class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = min(nums)
        currSum = 0

        for i in range(len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(maxSum, currSum)
        
        return maxSum

        
