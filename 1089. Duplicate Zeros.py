class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        l = len(arr)
        i = 0
        while i < l:
            if arr[i] == 0:
                arr.insert(i+1, 0)
                arr.pop()
                i += 1
            i += 1               