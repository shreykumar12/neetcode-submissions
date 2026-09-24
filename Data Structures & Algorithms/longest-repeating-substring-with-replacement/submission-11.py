class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            most = max(freq.values())
            if (r - l + 1) - most <= k:
                res = max(r - l + 1, res)
            else:
                freq[s[l]] -= 1
                l += 1
        
        return res
            