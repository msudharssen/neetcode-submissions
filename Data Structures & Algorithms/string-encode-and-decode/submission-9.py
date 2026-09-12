class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ""
        for word in strs:
            temp+=str(len(word))
            temp+="#"
            temp+=word
        
        return temp



    def decode(self, s: str) -> List[str]:

        begin = 0
        ans = []
        

        while begin < len(s):
            iterate = begin
            while s[iterate]!='#':
                iterate+=1
            
            length = int(s[begin:iterate])
            begin = iterate+1
            iterate = begin+length
            ans.append(s[begin:iterate])
            begin = iterate
        
        return ans


