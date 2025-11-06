# WAJP to count all prime numbers up to n. Count Primes
class Solution:
    def is_prime(self,n):
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
    def Count_Prime(self,N):
        count=0
        for i in range(N):
            if self.is_prime(i):
                count+=1
            i+=1
        return count
    

ob1=Solution()
N=20
print(ob1.Count_Prime(N))


