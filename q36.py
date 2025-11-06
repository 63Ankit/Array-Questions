#  WAJP to store first n palindrome numbers into array.
class Solution:
    def is_Palindrome(self,n):
        if str(n)!=str(n)[::-1]:
            return False
        return True
    def first_N_Palindrome(self,N):
        count=0
        arr=[0]*N
        j=0
        i=1
        while True:
            if count>=N:
                break
            if self.is_Palindrome(i):
                count+=1
                arr[j]=i
                j+=1
            i+=1
        return arr
    
ob1=Solution()
N=10
print(ob1.first_N_Palindrome(N))
        

            
