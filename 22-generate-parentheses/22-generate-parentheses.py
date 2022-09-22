class Solution:
    def generate(self,opn,close,res,string):
        if opn==0 and close==0:
            res.append(string)
            return
        
        if opn==close:
            self.generate(opn-1,close,res,string+"(")
        else:
            if opn>0:
                self.generate(opn-1,close,res,string+"(")
            self.generate(opn,close-1,res,string+")")
            
    def generateParenthesis(self, n: int) -> List[str]:
        opn=close=n
        res=[]
        self.generate(opn,close,res,"")
        return res