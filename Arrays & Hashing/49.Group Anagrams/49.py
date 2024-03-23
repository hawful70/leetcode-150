class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        if len(strs) == 1:
            return [[strs[0]]]

        
        frequency = defaultdict(list)
        
        for str in strs:
            sorted_str = "".join(sorted(str))
            frequency[sorted_str].append(str)

        return frequency.values()

