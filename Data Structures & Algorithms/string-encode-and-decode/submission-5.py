class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s))
            encoded += '#'
            encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            j = i
            while s[j] != '#':
                print(s[j])
                j += 1
            size = int(s[i:j])
            decoded.append(s[j + 1:j + size + 1])
            i = j + size + 1
        return decoded

