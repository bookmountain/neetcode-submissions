class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i, s in enumerate(strs):
            key = tuple(sorted(s))
            if key not in group:
                group[key] = []
            group[key].append(s)
        return list(group.values())
            
        