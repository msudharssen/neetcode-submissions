class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxValue = max(piles)
        start = 1
        end = maxValue 
        

        def traverse(perHour):

            total = 0
            for pile in piles:
                total+=math.ceil(pile/perHour)
            return total

        while start <= end:
            mid = start + (end-start)//2
            if traverse(mid) <= h:
                end = mid-1
            else:
                start = mid+1
        return start




