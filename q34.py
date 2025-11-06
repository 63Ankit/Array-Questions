# Q:34 WAPP to print and count all the palindrome number elements from array.
class Solution:
    def Is_palindrome(self,n):
        if str(n)!=str(n)[::-1]:
            
            return False
        return True
    def count(self,nums):
        count=0
        for i in range(len(nums)):
            if self.Is_palindrome(nums[i]):
                print(nums[i])
                count+=1
        return count
    
ob1=Solution()
nums=[121,434,654,868,9898]
print(ob1.count(nums))

    
