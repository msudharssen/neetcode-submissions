class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        for item in nums2:
            nums1.append(item)
        
        nums1.sort()
        if len(nums1) % 2 != 0:
            return nums1[len(nums1)//2]

        index = len(nums1) // 2

        return (nums1[index] + nums1[index-1]) / 2