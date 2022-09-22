class Solution(object):
    def shuffles(self,indx,nums,res):
        if len(nums)==indx:
            res.append(list(nums))
            return
        
        for i in range(indx,len(nums)):
            nums[i],nums[indx]=nums[indx],nums[i]
            self.shuffles(indx+1,nums,res)
            nums[i],nums[indx]=nums[indx],nums[i]
            
    def permute(self, nums):
        res=[]
        self.shuffles(0,nums,res)
        return res
        
        