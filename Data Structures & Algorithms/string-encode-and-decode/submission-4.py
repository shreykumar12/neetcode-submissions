class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            size = len(s)
            encoded += str(size)
            encoded += '#'
            encoded += s
        return encoded


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        
        while i  < len(s):
            j = i
            while s[j] != '#':
                j += 1
            size = int(s[i:j])
            res.append(s[j + 1: j + 1 + size])
            i = j + 1 + size
        return res

