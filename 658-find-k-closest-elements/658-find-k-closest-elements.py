class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start=0
        end=len(arr)-1
        while end-start>=k:
            if abs(arr[start]-x)>abs(arr[end]-x):
                start+=1
            else:
                end-=1
        
        return arr[start:end+1]