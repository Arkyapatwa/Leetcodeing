class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=0
        dif=nums[0]
        for i in range(1,len(nums)):
            a=nums[i]-dif
            if a>k:
                count+=1
                dif=nums[i]
        return count+1