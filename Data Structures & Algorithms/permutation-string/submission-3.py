class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False #Impossible to have permutation

        # Use arrays as freq counters - index = character (0 = a)
        s1Count, s2Count = [0] * 26, [0] * 26
        # Set up the counters with the vals in range (0 to len(s1))
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # Start with 0 matches and go through counters to 
        # identify matches 
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        
        # Sliding window starts here after we have got initial matches from the 
        # first 0 to len(s1) chars
        # Starting from where the first loop ended and going through the rest of s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: # Everything matches so we are good
                return True
            
            # Add char tot the window and update counts
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            # If the new count has messed up or fixed the matches apply
            # logic here 
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            # Same as above except this time for the character
            # we are removing and not adding
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        
        # after last iteration matches could == 26 so we check again here and
        # return the result
        return matches == 26
            
            