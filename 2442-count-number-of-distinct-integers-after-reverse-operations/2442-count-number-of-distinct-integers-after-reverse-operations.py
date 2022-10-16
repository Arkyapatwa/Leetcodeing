class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        arr=set(nums)
        for i in nums:
            arr.add(int(str(i)[::-1]))
        return len(arr)