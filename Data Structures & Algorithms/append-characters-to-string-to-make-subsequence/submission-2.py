class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        

        i = 0
        j = 0

        while i < len(t):
            while j < len(s):
                if t[i] == s[j]:
                    i += 1
                    if i >= len(t):
                        return len(t) - i
                j += 1
            return len(t) - i