class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start=0
        end=len(arr)-k
        while start<end:
            mid=(start+end)//2
            if x-arr[mid]<=arr[mid+k]-x:
                end-=1
            else:
                start+=1
        
        return arr[start:start+k]