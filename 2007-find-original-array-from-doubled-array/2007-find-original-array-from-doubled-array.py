class Solution:
    def findOriginalArray(self, c: List[int]) -> List[int]:
        if len(c)%2:
            return []
        c.sort()
        dic=collections.Counter(c)
        stack=[]
        n=len(c)
        for i in c:
            if i==0 and dic[i*2]>=2:
                stack.append(i)
                dic[i*2]-=2
            elif i>0 and dic[i] and dic[i*2]:
                stack.append(i)
                dic[i]-=1
                dic[i*2]-=1
            
        return stack if len(stack)==n//2 else []
                
        
                
                