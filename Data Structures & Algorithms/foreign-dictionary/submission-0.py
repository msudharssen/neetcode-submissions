class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {ch:set()for w in words for ch in w}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLength = min(len(w1), len(w2))
            if len(w1)>len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            for j in range(minLength):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res=[]

        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c]=True

            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True

            visited[c]=False
            res.append(c)
        
        for ch in adj:
            if dfs(ch):
                return ""
        
        return "".join(res[::-1])
        


