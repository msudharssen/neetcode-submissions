class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        answer = []
        info = defaultdict(list)

        for item in strs:
            tuTemp = tuple(sorted(item))
            if tuTemp in info:
                info[tuTemp].append(item)
            else:
                info[tuTemp].append(item)
        
        for k, v in info.items():
            answer.append(v)
        
        return answer