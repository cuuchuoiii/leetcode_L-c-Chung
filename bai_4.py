class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) > 1 :
            a = 0 
            for i in range(len(num)) :
                a = a + int(num[i])
            num = str(a)
        return int(num) 
