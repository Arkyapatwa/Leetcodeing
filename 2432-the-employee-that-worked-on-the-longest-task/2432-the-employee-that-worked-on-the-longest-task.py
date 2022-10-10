class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        
        key=[logs[0][0]]
        val=[logs[0][1]]
        
        for i in range(1,len(logs)):
            key.append(logs[i][0])
            val.append(logs[i][1]-logs[i-1][1])
        # print(key,val)
            
        Max=max(val)
        
        # if Max==min(val):
        #     return 0
        ans=sys.maxsize
        for i in range(len(key)):
            if val[i]==Max:
                if val.count(val[i])==1:
                    return key[i]
                else:
                    if key[i]<ans:
                        ans=key[i]
        return ans
            
        
        