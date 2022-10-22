class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for i,num in enumerate(nums):
            if num not in dic:
                dic[num]=[i]
            else:
                for indx in dic[num]:
                    if abs(indx-i)<=k:
                        return True
                dic[num]=dic.get(num)+[i]
        return False