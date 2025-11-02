# WAPP to check array is a palindromic array or not. Return true or false accordingly
'''
Input=[10,20,30,40,30,20,10]
Output=True
Input=[10,20,30,40,50,60,70]
Output=False
'''
class Solution:
    def Palindrome(self,nums):
        start=0
        end=len(nums)-1
        while(start<end):
            if nums[start]!=nums[end]:
                return "False"

            start+=1
            end-=1
        return "True"
ob1=Solution()
Input=[10,20,30,40,30,20,10]
print(ob1.Palindrome(Input))

