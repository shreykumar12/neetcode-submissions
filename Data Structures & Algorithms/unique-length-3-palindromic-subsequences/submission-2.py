class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)

        for m in range(len(s)):
            right[s[m]] -= 1
            if right[s[m]] == 0:
                right.pop(s[m])
            
            for i in range(26):
                c = chr(ord('a') + i)
                if c in left and c in right:
                    res.add((c, s[m]))
            
            left.add(s[m])

        return(len(res))
                
            