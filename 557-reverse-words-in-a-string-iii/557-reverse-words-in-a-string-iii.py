class Solution:
    def reverseWords(self, s: str) -> str:
        a=""
        stack=[]
        for i in s:
            if i==" ":
                stack.append(a[::-1])
                a=""
            else:
                a+=i
        return " ".join(stack)+" "+a[::-1] if stack else a[::-1]
            