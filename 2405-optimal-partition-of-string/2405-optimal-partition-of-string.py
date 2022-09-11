class Solution:
    def partitionString(self, s: str) -> int:
        # res=[]
        a=""
        count=0
        for i in range(len(s)):
            if s[i] not in a:
                a+=s[i]
            else:
                # res.append(a)
                count+=1
                a=s[i]
        # res.append(a)
        return count+1