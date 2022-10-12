class Solution:
    def largestPerimeter(self, sortednums: List[int]) -> int:
        sortednums.sort()
        for i in range(len(sortednums)-3,-1,-1):
            if sortednums[i]+sortednums[i+1]>sortednums[i+2]:
                return sortednums[i]+sortednums[i+1]+sortednums[i+2]
        return 0