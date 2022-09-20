class Solution(object):
    def subset(self,indx,arr,container,res):
        res.append(list(container))
        
        for i in range(indx,len(arr)):
            if i>indx and arr[i]==arr[i-1]:
                continue
            container.append(arr[i])
            self.subset(i+1,arr,container,res)
            container.pop()
            
    def subsetsWithDup(self, nums):
        res=[]
        nums.sort()
        self.subset(0,nums,[],res)
        return res