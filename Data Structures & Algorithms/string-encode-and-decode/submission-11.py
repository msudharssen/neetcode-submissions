class Solution:


    def encode(self, strs: List[str]) -> str:

        encodedStrings = ""
        
        for word in strs:
            encodedStrings+=str(len(word))
            encodedStrings+="#"
            encodedStrings+=word

        return encodedStrings

    def decode(self, s: str) -> List[str]:

        begin = 0
        answer = []
        

        while begin < len(s):
            iterate = begin
            while s[iterate]!='#':
                iterate+=1
            
            length = int(s[begin:iterate])
            begin = iterate+1
            iterate = begin+length
            answer.append(s[begin:iterate])
            begin = iterate
        
        
        return answer


