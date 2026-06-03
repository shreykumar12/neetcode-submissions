class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = Counter(s)
        tMap = Counter(t)

        return tMap == sMap
        