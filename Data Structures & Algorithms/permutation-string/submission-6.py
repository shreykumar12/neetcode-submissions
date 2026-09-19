class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars1 = [0] * 26
        chars2 = [0] * 26
        for c in s1:
            chars1[ord(c) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):
            chars2[ord(s2[r]) - ord('a')] += 1
            if (r - l + 1) > len(s1):
                chars2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if chars1 == chars2:
                return True
        
        return False


        