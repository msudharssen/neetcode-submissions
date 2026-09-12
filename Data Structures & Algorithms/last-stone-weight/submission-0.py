class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if(len(stones)==1):
            return stones[0]
        
        stones.sort()
        index = len(stones) - 1

        while(index > 0):
            stoneA = stones[index-1]
            stoneB = stones[index]
            print(stoneA, stoneB)
            if(stoneA == stoneB):
                 stones.pop()
                 stones.pop()
                 index-=2
            elif(stoneA < stoneB):
                stones[index] = stoneB - stoneA;
                stones.pop(index-1)
                stones.sort()
                index-=1
            else:
                stones[index-1] = stoneA - stoneB;
                stones.pop()
                stones.sort()
                index-=1
    
        if(len(stones)==1):
             return stones[0]
        
        return 0
            
        