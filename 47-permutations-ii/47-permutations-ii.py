class Solution:
    def permute(self,indx,nums,arr):
        if len(nums)==indx and nums not in arr:
            arr.append(list(nums))
            return
        
        for i in range(indx,len(nums)):
            nums[i],nums[indx]=nums[indx],nums[i]
            self.permute(indx+1,nums,arr)
            nums[i],nums[indx]=nums[indx],nums[i]
                
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        self.permute(0,nums,arr)
        return arr