# Q:32 WAPP to print and count all the prime number elements from array.
class Solution:
    def isPrime(self,n):
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
    
        
        

    def Prime_Number(self,nums):
        c=0
        for i in range(len(nums)):
                
            if self.isPrime(nums[i]):
                print(nums[i])
                c+=1
        return c

ob1=Solution()
nums=[10,20,30,11,13,17,1,2,3,4,5]
print(ob1.Prime_Number(nums))
        
