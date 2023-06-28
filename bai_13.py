class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        return map({x : i+1 for i , x in enumerate(sorted(set(arr)))}.get, arr)