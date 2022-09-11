class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic={}
        flag=1
        
        for i in range(len(nums)):
            if nums[i]%2==0:
                if nums[i] not in dic:
                    dic[nums[i]]=1
                else:
                    dic[nums[i]]+=1
                
        if not dic:
            return -1
        else:
            Min=sys.maxsize
            Max=max(dic.values())
            for key,val in dic.items():
                if val==Max:
                    Min=min(Min,key)
            return Min