class Solution(object):
    def combinations(self,indx,arr,res,ds):
        if indx==len(arr):
            res.append(list(ds))
            return
        
        ds.append(arr[indx])
        self.combinations(indx+1,arr,res,ds)
        ds.pop()
        
        self.combinations(indx+1,arr,res,ds)
        
    def subsets(self, nums):
        res=[]
        self.combinations(0,nums,res,[])
        return res
        