class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        pairs = {'I' : 1, 'V' : 5, 'X': 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        
        i = 0
        while i < len(s):
            if s[i] == 'I':
                add = pairs[s[i]]
                if i < len(s) - 1:
                    if s[i + 1] == 'V' or s[i + 1] == 'X':
                        add = pairs[s[i + 1]] - pairs[s[i]]
                        i += 1
                res += add
            elif s[i] == 'X':
                add = pairs[s[i]]
                if i < len(s) - 1:
                    if s[i + 1] == 'L' or s[i + 1] == 'C':
                        add = pairs[s[i + 1]] - pairs[s[i]]
                        i += 1
                res += add
            elif s[i] == 'C':
                add = pairs[s[i]]
                if i < len(s) - 1:
                    if s[i + 1] == 'D' or s[i + 1] == 'M':
                        add = pairs[s[i + 1]] - pairs[s[i]]
                        i += 1
                res += add
            elif s[i] == 'V':
                res += pairs[s[i]]
            elif s[i] == 'L':
                res += pairs[s[i]] 
            elif s[i] == 'D':
                res += pairs[s[i]]
            elif s[i] == 'M':
                res += pairs[s[i]]
            i += 1

        return res