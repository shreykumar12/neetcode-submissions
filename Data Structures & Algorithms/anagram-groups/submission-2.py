class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            groups[tuple(chars)].append(s)
        for val in groups.values():
            res.append(val)
        return res