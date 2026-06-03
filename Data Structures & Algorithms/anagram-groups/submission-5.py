class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        
        for val in groups.values():
            res.append(val)

        return res