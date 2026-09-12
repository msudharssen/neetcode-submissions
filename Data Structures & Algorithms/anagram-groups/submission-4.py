class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        info = defaultdict(list)
        for word in strs:
            temp = [0] * 26
            for char in word:
                temp[ord(char)-ord('a')]+=1
            info[tuple(temp)].append(word)
        
        return list(info.values())

