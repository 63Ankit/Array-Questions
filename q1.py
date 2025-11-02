# Q:1 Print biggest element ,smallest elements and their difference from the given array
# A=[10,30,54,87,56,89,45]
'''
89
10
'''
class Solution:
    def number(self,nums):
        biggest=nums[0]
        smallest=nums[0]
        for i in range(len(nums)):
            if nums[i]>biggest:
                biggest=nums[i]
            if nums[i]<smallest:
                smallest=nums[i]
        return biggest,smallest
ob1=Solution()
a1=[10,30,54,87,56,89,45]
bi1,slamm=ob1.number(a1) 
print(bi1) 
print(slamm)    

