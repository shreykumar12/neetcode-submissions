class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub= set()
        maxSub = 0
        l = 0
        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            maxSub = max(maxSub, r - l + 1)
        
        return maxSub