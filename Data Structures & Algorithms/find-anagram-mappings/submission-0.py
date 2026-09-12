class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        info = defaultdict()
        for ind, num in enumerate(nums2):
            info[num]=ind

        output=[-1]*len(nums1)
        for ind,num in enumerate(nums1):
            output[ind]=info[num]
        return output