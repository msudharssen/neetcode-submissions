class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writeIndex = 0

        for r in range(len(nums)):
            if nums[r]!=val:
                nums[writeIndex] = nums[r]
                writeIndex+=1
        return writeIndex