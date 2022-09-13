class Solution:
    def letters(self,res,indx,ans,digits,dic):
        if len(digits)==indx:
            res.append("".join(ans))
            return
    
        s=dic[int(digits[indx])]
        for i in range(len(s)):
            ans.append(s[i])
            self.letters(res,indx+1,ans,digits,dic)
            ans.pop()
            
            
    def letterCombinations(self, digits: str) -> List[str]:
        dic={
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        res=[]
        if len(digits)==0:
            return res
        self.letters(res,0,[],digits,dic)
        return res