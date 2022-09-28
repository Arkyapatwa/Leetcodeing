class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic={}
        for i,ele in enumerate(nums):
            if ele in dic:
                dic[ele]=dic[ele]+[i]
            else:
                dic[ele]=[i]
                
        res=sys.maxsize
        
        lengths=[len(i) for i in dic.values()]
        
        for key,val in dic.items():
            if len(val)==max(lengths):
                l=val[-1]-val[0]+1
                res=min(res,l)
        
        return res