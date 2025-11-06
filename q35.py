#Q:35--> WAPP to store first n prime numbers into array.

class Solution:
    def is_Prime(self,n):
        if n<2:
            return False
        if n==2 or n==3:
            return True
        if n%2==0:
            return False
        i=3
        while i*i<=n:
            if n%i==0:
                return False
            i+=2
        return True
    def First_N_Prime_Number(self,N):
        count=0
        arr=[0]*N
        j=0
        i=1
        while True:
            if count>=N:
                break
            if self.is_Prime(i):
                count+=1
                arr[j]=i
                j+=1
            i+=1
        return arr
    
ob1=Solution()
N=10
print(ob1.First_N_Prime_Number(N))




