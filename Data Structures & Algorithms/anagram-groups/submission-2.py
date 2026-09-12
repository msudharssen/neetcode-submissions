class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        answer = []
        info = defaultdict(list)

        for item in strs:
            tuTemp = tuple(sorted(item))
            info[tuTemp].append(item)
            
        for k, v in info.items():
            answer.append(v)
        
        return answer