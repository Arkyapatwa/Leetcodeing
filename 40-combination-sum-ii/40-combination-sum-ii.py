# 1 1 2 5 6 7 10
class Solution(object):
    def combinations(self,indx,arr,target,res,ds):
        
        if target==0:
            res.append(list(ds))
            return
        
        for i in range(indx,len(arr)):
            if i>indx and arr[i]==arr[i-1]:
                continue
            if arr[i]>target:
                break
            ds.append(arr[i])
            self.combinations(i+1,arr,target-arr[i],res,ds)
            ds.pop()
            
        
        
    def combinationSum2(self, candidates, target):
        res=[]
        candidates.sort()
        self.combinations(0,candidates,target,res,[])
        return res