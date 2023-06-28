class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr = []
        seen = set()
        for a in nums :
            if a in seen :
                arr.append(a)
            else :
                seen.add(a)
        return arr
        