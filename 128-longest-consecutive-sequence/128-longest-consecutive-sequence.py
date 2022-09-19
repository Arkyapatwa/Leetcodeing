class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        # nums.sort()
        # count=1
        # Max=1
        # for i in range(len(nums)-1):
        #     if nums[i]!=nums[i+1]:
        #         if nums[i]+1==nums[i+1]:
        #             count+=1
        #         else:
        #             Max=max(count,Max)
        #             count=1
        # return max(Max,count)
        setnums=set(nums)
        Max=0
        for sn in setnums:
            if sn-1 not in setnums:
                count=1
                cur=sn
                while cur+1 in setnums:
                    count+=1
                    cur+=1
                Max=max(count,Max)
        return Max
            