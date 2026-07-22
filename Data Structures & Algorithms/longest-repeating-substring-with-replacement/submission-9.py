class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Use a freq map to trasck counts of chars in curent window
        # if window is invalid we trim from the left until it becomes 
        # a valid window
        # otherwise we check and update the result because our window is now valid

        freq = {}
        l = 0
        res = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res                