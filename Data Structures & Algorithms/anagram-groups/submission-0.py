
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        set1 = defaultdict(list)
        answer = []

        for item in strs:
            temp = tuple(sorted(item))
            if temp in set1:
                tempList = set1[temp]
                tempList.append(item)
            else:
                set1[temp] = list()
                temporary = set1[temp]
                temporary.append(item)
        
        for key, value in set1.items():
            answer.append(value)
        
        return answer
