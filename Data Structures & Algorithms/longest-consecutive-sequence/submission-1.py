class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        
        for n in nums:
            if n - 1 in nums:
                continue
            else:
                curr = 1
                nxt = n + 1
                while nxt in nums:
                    curr += 1
                    nxt += 1
                longest = max(curr, longest)
        return longest

                

        