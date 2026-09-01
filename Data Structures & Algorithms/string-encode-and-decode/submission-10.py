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
        decode = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            size = int(s[i:j])
            decode.append(s[j + 1:j + size + 1])
            i = (j + size + 1)
        return decode

            
            
