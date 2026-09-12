class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        info = defaultdict(list)
        for word in strs:
            letterArray = [0]*26
            for ch in word:
                letterArray[ord('a')-ord(ch)]+=1
            info[tuple(letterArray)].append(word)
        return list(info.values())
    

    
