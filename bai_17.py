class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a,b = nums[0],nums[0]
        for i in range(1,len(nums)):
            a = max(nums[i],a+nums[i])
            b = max(a,b)
        return b