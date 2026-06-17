class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for word in strs:
            sorted_keys = "".join(sorted(word))
            groups[sorted_keys].append(word)  
        return list(groups.values())
