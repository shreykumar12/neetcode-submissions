class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            size = len(s)
            res += str(size)
            res += "#"
            res += s
        return res
            


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j]!= "#":
                j += 1
            size = int(s[i:j])
            i = j + 1
            res.append(s[i:size + i])
            i += size

        return res

            


            


            
        
