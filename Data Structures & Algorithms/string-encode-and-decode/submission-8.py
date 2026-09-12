class Solution:


    def encode(self, strs: List[str]) -> str:
        temp = ""
        for word in strs:
            temp+=str(len(word))
            temp+="#"
            temp+=word
        return temp
    def decode(self, s: str) -> List[str]:
        answer = []
        i=0
        
        while i < len(s):
            j = i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            answer.append(s[i:j])
            i = j
        
        return answer
            


