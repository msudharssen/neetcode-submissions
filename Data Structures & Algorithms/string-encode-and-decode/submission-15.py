class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word))
            res += '#'
            res += word
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        start = 0

        while start < len(s):
            begin = start
            while s[begin]!="#":
                begin+=1
            length = int(s[start:begin])
            start = begin+1
            begin = start + length
            res.append(s[start:begin])
            start = begin
        return res

        
