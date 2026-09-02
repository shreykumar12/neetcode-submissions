class Solution:
    def isPalindrome(self, s: str) -> bool:
        sClean = ""

        for c in s:
            if c.isalnum():
                sClean += c.lower()

        l, r = 0, len(sClean) - 1
        while l < r:
            if sClean[l] != sClean[r]:
                return False
            l += 1
            r -= 1
        
        return True
