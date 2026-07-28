class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        pairs = {'I' : 1, 'V' : 5, 'X': 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        i = 0

        while i < len(s):
            if i < len(s) - 1 and pairs[s[i]] < pairs[s[i + 1]]:
                res += pairs[s[i + 1]] - pairs[s[i]]
                i += 1
            else:
                res += pairs[s[i]]
            i += 1
        
        return res