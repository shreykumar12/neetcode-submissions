class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            # left sorted portion
            if nums[m] >= nums[l]:
                # value in left sorted portion
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                # not in left portion
                else:
                    l = m + 1
            # right sorted portion
            else:
                # value in right sorted portion
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                # not in right portion
                else:
                    r = m - 1
        
        return -1
