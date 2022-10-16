class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if not num:
            return True
        for i in range(num//2,num):
            s=i+int(str(i)[::-1])
            if s==num:
                return True
        return False