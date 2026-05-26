class Solution:
    def isPalindrome(self, s: str) -> bool:
        sCleaned = ""
        for c in s:
            if c.isalnum():
                sCleaned += c.lower()
        
        l, r = 0, len(sCleaned) - 1
        
        while l <= r:
            if sCleaned[l] != sCleaned[r]:
                return False
            l += 1
            r -= 1
        return True