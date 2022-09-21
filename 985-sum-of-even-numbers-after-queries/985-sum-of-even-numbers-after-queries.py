class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s=0
        for i in nums:
            if i%2==0:
                s+=i
                
        res=[]
        for query in queries:
            if nums[query[1]]%2==0:
                flag=1
            else:
                flag=0
            i=query[1] 
            temp=nums[i]
            nums[i]+=query[0]
            
            if nums[i]%2==0 and flag==0:
                s+=nums[i]
                res.append(s)
            elif nums[i]%2==0 and flag==1:
                s+=query[0]
                res.append(s)
            elif nums[i]%2!=0 and flag==1:
                s-=temp
                res.append(s)
            else:
                res.append(s)
        return res