class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # loop through s and t
        # look for a subsequence if we find one retunr 0
        # if we dont, then wherever we stop, return the remanining length of t (len(t) - i)
        

        i = 0
        j = 0

        while i < len(t):
            while j < len(s):
                if s[j] == t[i]:
                    i += 1
                    if i >= len(t):
                        return len(t) - i
                j += 1
            return len(t) - i
    
            
        



        
        
