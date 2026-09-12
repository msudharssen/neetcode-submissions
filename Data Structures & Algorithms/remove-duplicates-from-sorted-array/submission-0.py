class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writeIndex = 1

        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[writeIndex]=nums[r]
                writeIndex+=1
        
        return writeIndex
