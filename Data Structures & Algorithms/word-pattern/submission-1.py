class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map1 = {}
        map2 = {}
        
        arr = s.split(" ")
        if len(pattern)!=len(arr):
            return False
        print(arr)
        for i, ch in enumerate(pattern):
            if ch in map1 and map1[ch]!=arr[i]:
                return False
            elif arr[i] in map2 and map2[arr[i]]!=ch:
                return False
            else:
                map1[ch]=arr[i]
                map2[arr[i]]=ch
            
        
        return True
