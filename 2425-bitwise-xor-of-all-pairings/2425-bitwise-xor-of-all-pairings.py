class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        s=0
        if len(nums2)%2:
            for i in nums1:
                s^=i
        else:
            s=0
        if len(nums1)%2:
            for i in nums2:
                s^=i
        else:
            s^=0
        return s