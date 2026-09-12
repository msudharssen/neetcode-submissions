class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        info = defaultdict(list)
        for word in strs:
            temp = str(sorted(word))
            info[temp].append(word)
        
        return list(info.values())

