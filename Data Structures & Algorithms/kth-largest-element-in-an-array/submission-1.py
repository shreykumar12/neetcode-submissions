class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 2 pointer on each end
        # keep track of the max, if we find something higher
        # update the max and see what the k from that max is
        nums.sort()
        f, s = 0, 0
        while k > 0:
            f += 1
            k -= 1

        while f < len(nums):
            f += 1
            s += 1
        
        return nums[s]
            
            
        
        
        