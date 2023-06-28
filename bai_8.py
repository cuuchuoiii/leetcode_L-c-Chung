class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted( nums1 + nums2 )
        n = len(nums)

        if n % 2 == 0 :
            a = (nums[n//2] + nums[n//2-1]) /2 
        else :
            a = nums[n//2]
        return a

            

            
            