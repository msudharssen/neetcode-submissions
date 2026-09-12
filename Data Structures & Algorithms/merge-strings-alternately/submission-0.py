class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''

        word1Index = 0
        word2Index = 0

        while word1Index < len(word1) and word2Index < len(word2):
            output += word1[word1Index]
            output += word2[word2Index]
            word1Index+=1
            word2Index+=1
        
        while word1Index < len(word1):
            output += word1[word1Index]
            word1Index+=1
        
        while word2Index < len(word2):
            output += word2[word2Index]
            word2Index+=1
        
        return output
        
