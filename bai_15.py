def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class Solution:
    def countPrimes(self, n: int) -> int:
        arr = [1]*n
        if n>1:
            arr[1]=0
        if n==0 or n==1:
            return 0 

        for i in range(2,math.ceil(math.sqrt(n))):
            if arr[i]==0:
                continue
            for j in range(i,1+math.ceil(n/i)):
                if i*j>=n:
                    continue
                arr[j*i]=0
        return sum(arr)-1