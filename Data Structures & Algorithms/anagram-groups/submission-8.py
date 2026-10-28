class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            chars = [0] * 26
            for c in word:
                chars[ord(c) - ord('a')] += 1
            groups[tuple(chars)].append(word)
        return list(groups.values())