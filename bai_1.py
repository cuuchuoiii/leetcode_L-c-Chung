class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            a = nums.index(target)
            return a 
        else:
            nums.append(target) 
            nums.sort()
            a = nums.index(target)
            return a 