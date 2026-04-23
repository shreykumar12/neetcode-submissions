class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            if tuple(chars) in groups:
                groups[tuple(chars)].append(s)
            else:
                groups[tuple(chars)] = [s]
        for val in groups.values():
            res.append(val)
        return res