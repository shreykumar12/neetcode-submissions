class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1chars = [0] * 26
        s2chars = [0] * 26

        for c in s1:
            s1chars[ord(c) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):
            s2chars[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 > len(s1):
                s2chars[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if s1chars == s2chars:
                return True
        
        return False


