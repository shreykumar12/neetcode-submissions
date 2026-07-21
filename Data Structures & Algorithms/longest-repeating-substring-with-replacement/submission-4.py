class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        l = 0

        for r in range(len(s)):
            # Add current char to the freq map
            freq[s[r]] = freq.get(s[r], 0) + 1
            # Chechk if the current window is valid
            # len(window) - maxCharFreq <= k is valid
            # Means we have at most k replacements in the window
            if (r - l + 1) - max(freq.values()) <= k:
                print(r, l)
                res = max(res, r - l + 1)
            # Else we don't have enough replacements/invalid window
            # So we trim the window from the left updating freq
            while (r - l + 1) - max(freq.values()) > k:
                # Decrement the count of the char leaving the window
                # Then update the window
                freq[s[l]] -= 1
                l += 1
        return res
            
